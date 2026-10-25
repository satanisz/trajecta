"""Small dense CTMC reference using row vectors: dp/dt = p Q.

Uniformization terms count Poisson events, including virtual self-transitions.
They are not physical jump trajectories or the Stanisz-Cetnar TTA algorithm.
"""
from dataclasses import dataclass
import math
import random
from typing import Sequence

Matrix = list[list[float]]


def generator(rates: Sequence[Sequence[float]]) -> Matrix:
    """Build Q from nonnegative off-diagonal rates (input diagonal must be zero)."""
    n = len(rates)
    if n == 0 or any(len(row) != n for row in rates):
        raise ValueError('rates must be nonempty and square')
    if any(not math.isfinite(x) or x < 0 for row in rates for x in row):
        raise ValueError('rates must be finite and nonnegative')
    if any(rates[i][i] != 0 for i in range(n)):
        raise ValueError('rates diagonal must be zero')
    q = [list(map(float, row)) for row in rates]
    for i in range(n):
        q[i][i] = -math.fsum(q[i])
    validate_generator(q)
    return q


def validate_generator(q: Sequence[Sequence[float]]) -> None:
    n = len(q)
    if n == 0 or any(len(row) != n for row in q):
        raise ValueError('Q must be nonempty and square')
    for i, row in enumerate(q):
        if any(not math.isfinite(x) for x in row):
            raise ValueError('Q must be finite')
        if row[i] > 0 or any(x < 0 for j, x in enumerate(row) if j != i):
            raise ValueError('Q has invalid signs')
        if abs(math.fsum(row)) > 1e-12 * max(1, -row[i]):
            raise ValueError('Q rows must sum to zero')


def _probability(p, n):
    if len(p) != n or any(not math.isfinite(x) or x < 0 for x in p):
        raise ValueError('invalid probability vector')
    if not math.isclose(math.fsum(p), 1.0, abs_tol=1e-10, rel_tol=0):
        raise ValueError('probabilities must sum to one')


def _horizon(t):
    if not math.isfinite(t) or t < 0:
        raise ValueError('time must be finite and nonnegative')


def uniformization_terms(p, q, t, max_events):
    """Return vectors exp(-nu*t)*(nu*t)^k/k! * p R^k for k=0..max_events.

    Only nu*t <= 50 is accepted; use propagate() for larger horizons.
    The missing Poisson mass is reported separately and never renormalized away.
    """
    validate_generator(q); _probability(p, len(q)); _horizon(t)
    if not isinstance(max_events, int) or isinstance(max_events, bool) or max_events < 0:
        raise ValueError('max_events must be a nonnegative integer')
    nu = max(-q[i][i] for i in range(len(q)))
    mu = nu * t
    if not math.isfinite(mu) or mu > 50:
        raise ValueError('nu*t exceeds 50; split the interval')
    if mu == 0:
        return [list(p)] + [[0.0]*len(q) for _ in range(max_events)], 0.0
    r = [[float(i == j) + q[i][j]/nu for j in range(len(q))] for i in range(len(q))]
    v = list(p); weight = math.exp(-mu); weights = []; terms = []
    for k in range(max_events + 1):
        weights.append(weight)
        terms.append([weight*x for x in v])
        v = [math.fsum(v[i]*r[i][j] for i in range(len(q))) for j in range(len(q))]
        weight *= mu/(k + 1)
    return terms, max(0.0, 1.0-math.fsum(weights))


def propagate(p, q, t, tolerance=1e-12):
    """Propagate a probability row vector, returning (subprobabilities, tail_bound).

    Interval splitting avoids exponential underflow. An analytic Chernoff bound
    selects the truncation order. Roundoff is not included in tail_bound.
    """
    validate_generator(q); _probability(p, len(q)); _horizon(t)
    if not math.isfinite(tolerance) or not 1e-14 <= tolerance <= 1e-3:
        raise ValueError('tolerance must be between 1e-14 and 1e-3')
    nu = max(-q[i][i] for i in range(len(q)))
    total = nu*t
    if not math.isfinite(total) or total > 200_000:
        raise ValueError('horizon too large for this educational dense solver')
    if total == 0: return list(p), 0.0
    steps = max(1, math.ceil(total/20))
    mu = total/steps
    k = math.ceil(mu)
    # P(Poisson(mu)>=m) <= exp(-mu)*(e*mu/m)^m for m>mu.
    while -mu + (k+1)*(1+math.log(mu/(k+1))) > math.log(tolerance/steps):
        k += 1
    bound = math.exp(-mu + (k+1)*(1+math.log(mu/(k+1)))) * steps
    r = [[float(i == j)+q[i][j]/nu for j in range(len(q))] for i in range(len(q))]
    result = list(p)
    for _ in range(steps):
        v = result; weight = math.exp(-mu); terms = []
        for event in range(k+1):
            terms.append([weight*x for x in v])
            v = [math.fsum(v[i]*r[i][j] for i in range(len(q))) for j in range(len(q))]
            weight *= mu/(event+1)
        result = [math.fsum(term[j] for term in terms) for j in range(len(q))]
    return result, bound


@dataclass(frozen=True)
class Trajectory:
    initial: int
    jumps: tuple[tuple[float, int], ...]
    horizon: float


def _state(s, n):
    if not isinstance(s, int) or isinstance(s, bool) or not 0 <= s < n:
        raise ValueError('state index out of range')


def simulate(q, initial, horizon, rng: random.Random, max_jumps=100_000):
    """Gillespie direct simulation, with the last interval right-censored."""
    validate_generator(q); _state(initial, len(q)); _horizon(horizon)
    state = initial; time = 0.0; jumps = []
    while time < horizon:
        rate = -q[state][state]
        if rate == 0: break
        next_time = time + rng.expovariate(rate)
        if next_time >= horizon: break
        if next_time <= time:
            raise ArithmeticError('holding time below floating point resolution')
        if len(jumps) >= max_jumps:
            raise RuntimeError('max_jumps exceeded')
        targets = [j for j in range(len(q)) if j != state and q[state][j] > 0]
        state = rng.choices(targets, weights=[q[state][j] for j in targets], k=1)[0]
        time = next_time; jumps.append((time, state))
    return Trajectory(initial, tuple(jumps), horizon)


def sufficient_statistics(paths, n):
    """Count real jumps and exposure, including censored terminal intervals."""
    if not isinstance(n, int) or n < 1: raise ValueError('invalid state count')
    exposure = [0.0]*n; counts = [[0]*n for _ in range(n)]
    for path in paths:
        _state(path.initial, n); _horizon(path.horizon)
        state = path.initial; previous = 0.0
        for time, destination in path.jumps:
            _state(destination, n)
            if not math.isfinite(time) or not previous < time < path.horizon or destination == state:
                raise ValueError('invalid real-jump trajectory')
            exposure[state] += time-previous
            counts[state][destination] += 1
            state = destination; previous = time
        exposure[state] += path.horizon-previous
    return counts, exposure


def fit_generator(paths, n):
    """Fully observed homogeneous CTMC MLE q_ij=N_ij/T_i.

    Refuses unobserved rows: zero exposure is not evidence of an absorbing state.
    """
    counts, exposure = sufficient_statistics(paths, n)
    if any(t <= 0 for t in exposure):
        raise ValueError('each state needs positive observed exposure')
    return generator([[counts[i][j]/exposure[i] if i != j else 0.0 for j in range(n)] for i in range(n)])


def negative_log_likelihood(paths, q):
    """Conditional on initial states and observation horizons; includes censoring."""
    validate_generator(q)
    counts, exposure = sufficient_statistics(paths, len(q))
    result = math.fsum(-q[i][i]*exposure[i] for i in range(len(q)))
    for i in range(len(q)):
        for j in range(len(q)):
            if i != j and counts[i][j]:
                if q[i][j] == 0: return math.inf
                result -= counts[i][j]*math.log(q[i][j])
    return result

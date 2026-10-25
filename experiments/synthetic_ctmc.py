"""Simulate independent trajectories, fit a CTMC, and evaluate held-out paths."""
import argparse
import json
import random
from pathlib import Path
from trajecta.ctmc import generator, simulate, fit_generator, propagate, negative_log_likelihood


def run(seed=42, train_size=2000, test_size=500):
    if train_size < 3 or test_size < 1:
        raise ValueError('train_size >= 3 and test_size >= 1 required')
    q = generator([[0, .8, .2], [.3, 0, .5], [.4, .1, 0]])
    train_rng = random.Random(seed); test_rng = random.Random(seed+1)
    train = [simulate(q, i%3, 5., train_rng) for i in range(train_size)]
    test = [simulate(q, i%3, 5., test_rng) for i in range(test_size)]
    fitted = fit_generator(train, 3)
    baseline = generator([[0, 1., 1.], [1., 0, 1.], [1., 1., 0]])
    expected, tail = propagate([1., 0., 0.], q, 5.)
    predicted, fit_tail = propagate([1., 0., 0.], fitted, 5.)
    return {'seed':seed, 'train_size':train_size, 'test_size':test_size,
            'true_generator':q, 'fitted_generator':fitted,
            'rate_mae':sum(abs(q[i][j]-fitted[i][j]) for i in range(3) for j in range(3) if i!=j)/6,
            'held_out_nll_per_path':{name:negative_log_likelihood(test, model)/test_size
                 for name, model in [('oracle',q),('mle',fitted),('unit_rate_baseline',baseline)]},
            'endpoint_true':expected, 'endpoint_fitted':predicted,
            'endpoint_l1_error':sum(abs(a-b) for a,b in zip(expected,predicted)),
            'mass_error':abs(1-sum(predicted)), 'poisson_tail_bound':max(tail,fit_tail),
            'scope':'Fully observed stationary CTMC; no neural encoder, causal effect estimate, or TTA implementation.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=42)
    parser.add_argument('--train-size',type=int,default=2000)
    parser.add_argument('--test-size',type=int,default=500)
    parser.add_argument('--output',type=Path,default=Path('outputs/synthetic_ctmc.json'))
    args=parser.parse_args()
    result=run(args.seed,args.train_size,args.test_size)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()

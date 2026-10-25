import math
import random
import unittest
from trajecta.ctmc import (Trajectory, generator, propagate, uniformization_terms,
                           simulate, sufficient_statistics, fit_generator,
                           negative_log_likelihood)


class CTMCTest(unittest.TestCase):
    def test_two_state_closed_form(self):
        a,b=1.7,.4
        q=generator([[0,a],[b,0]])
        for t in [0,.01,1,50,500]:
            p,bound=propagate([1,0],q,t)
            expected=b/(a+b)+a/(a+b)*math.exp(-(a+b)*t)
            self.assertAlmostEqual(p[0],expected,places=10)
            self.assertLessEqual(abs(sum(p)-1),bound+1e-12)

    def test_absorbing_and_zero_generator(self):
        p, bound = propagate([0,1],generator([[0,1],[0,0]]),20)
        self.assertEqual(p[0],0.)
        self.assertLessEqual(abs(p[1]-1),bound+1e-14)
        self.assertEqual(propagate([.3,.7],[[0,0],[0,0]],20)[0],[.3,.7])

    def test_probability_mass_of_truncated_terms(self):
        q=generator([[0,2],[1,0]])
        terms,tail=uniformization_terms([1,0],q,1,3)
        self.assertAlmostEqual(sum(map(sum,terms))+tail,1.)
        self.assertGreater(tail,.1)
        full,_=propagate([1,0],q,1)
        partial=[sum(row[i] for row in terms) for i in range(2)]
        self.assertTrue(all(a<=b+1e-12 for a,b in zip(partial,full)))

    def test_terminal_censoring_is_counted(self):
        path=Trajectory(0,((2.,1),),5.)
        counts,times=sufficient_statistics([path],2)
        self.assertEqual(times,[2.,3.])
        self.assertEqual(counts,[[0,1],[0,0]])
        self.assertEqual(fit_generator([path],2),[[-.5,.5],[0.,-0.]])
        self.assertAlmostEqual(negative_log_likelihood([path],generator([[0,2],[1,0]])),7-math.log(2))

    def test_unobserved_row_is_not_absorbing(self):
        with self.assertRaises(ValueError): fit_generator([Trajectory(0,(),5)],2)

    def test_impossible_jump_has_infinite_nll(self):
        self.assertEqual(negative_log_likelihood([Trajectory(0,((1,1),),2)],[[0,0],[0,0]]),math.inf)

    def test_invalid_inputs(self):
        for q in [[],[[1]],[[0,-1],[0,0]],[[0,float('nan')],[0,0]]]:
            with self.assertRaises(ValueError): generator(q)
        for t in [-1,float('nan'),float('inf')]:
            with self.assertRaises(ValueError): propagate([1],[[0]],t)
        with self.assertRaises(ValueError): propagate([.5],[[0]],1)
        with self.assertRaises(ValueError): sufficient_statistics([Trajectory(0,((1,0),),2)],1)

    def test_simulation_endpoint_matches_master_equation(self):
        q=generator([[0,1],[.3,0]])
        rng=random.Random(123)
        paths=[simulate(q,0,2,rng) for _ in range(6000)]
        observed=sum((p.jumps[-1][1] if p.jumps else p.initial)==0 for p in paths)/len(paths)
        expected,_=propagate([1,0],q,2)
        self.assertLess(abs(observed-expected[0]),.025)

    def test_recovery_and_held_out_likelihood(self):
        from experiments.synthetic_ctmc import run
        result=run()
        self.assertLess(result['rate_mae'],.04)
        nll=result['held_out_nll_per_path']
        self.assertLess(nll['mle'],nll['unit_rate_baseline'])

    def test_chronological_period_composition(self):
        q1=generator([[0,1],[0,0]]); q2=generator([[0,0],[1,0]])
        p,_=propagate([1,0],q1,1)
        p,_=propagate(p,q2,1)
        self.assertAlmostEqual(p[1],(1-math.exp(-1))*math.exp(-1),places=10)
        reverse,_=propagate([1,0],q2,1)
        reverse,_=propagate(reverse,q1,1)
        self.assertGreater(abs(p[1]-reverse[1]),.2)


if __name__=='__main__': unittest.main()

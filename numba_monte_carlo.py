import random
import timeit
import numpy as np
import numba
from statistics import mean

@numba.jit
def numba_direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x**2 + y**2 < 1.0:
            n_hits += 1
    return n_hits
    
def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x**2 + y**2 < 1.0:
            n_hits += 1
    return n_hits    
    
n_runs = 1000
n_trials = 4000
pi_approx = []

print("Running naive tests")
start_time = timeit.default_timer()
for run in range(n_runs):
    pi_approx.append(4.0 * direct_pi(n_trials) / float(n_trials))
elapsed_time = timeit.default_timer() - start_time            
print("Approximation to pi: ", mean(pi_approx))
print("Time taken: ", "%1.2f seconds" % elapsed_time)

print("Running numba-optimized tests")
start_time = timeit.default_timer()
for run in range(n_runs):
    pi_approx.append(4.0 * numba_direct_pi(n_trials) / float(n_trials))
elapsed_time = timeit.default_timer() - start_time            
print("Approximation to pi: ", mean(pi_approx))
print("Time taken: ", "%1.2f seconds" % elapsed_time)


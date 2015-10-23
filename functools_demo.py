import functools
import timeit
import numpy as np

def RecursiveFib(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return RecursiveFib(n-1) + RecursiveFib(n-2)

@functools.lru_cache(maxsize=4)	
def MemoRecursiveFib(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return MemoRecursiveFib(n-1) + MemoRecursiveFib(n-2)
	

def DynamicFib(n):
	a, b = 1, 1
	if n < 3:
		return 1
	for k in range(n-2):
		a, b = b, a+b
	return b
	
def NumpyMatrixFib(n):
	fib = np.array([[1, 1], [1, 0]], dtype=object)
	fib = np.linalg.matrix_power(fib, n)
	return fib[0,1]

start_time = timeit.default_timer()	
DynamicFib(100000)
elapsed = timeit.default_timer() - start_time
print("Elapsed time for dynamic solution:", elapsed)

start_time = timeit.default_timer()	
for j in range(1,100001):
	MemoRecursiveFib(j)
elapsed = timeit.default_timer() - start_time
print("Elapsed time for memoized solution:", elapsed)
 
start_time = timeit.default_timer()	
NumpyMatrixFib(100000)
elapsed = timeit.default_timer() - start_time
print("Elapsed time for numpy matrix solution:", elapsed)
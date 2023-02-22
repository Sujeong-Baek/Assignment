# sieve1.py
# Compute prime numbers using Sieve of Erathostenes

# from listset import set

import sys
import math
import time


def sieve(n):
    s = set(range(2, n+1))
    sqrtn = int(math.sqrt(n))
    for i in range(2, sqrtn+1):
        if i in s:
            k = i**2
            while k <= n:
                s.discard(k)
                k += i
    return s

if len(sys.argv) == 2:
    num = int(sys.argv[1])
else:
    num = 100

startTime = time.perf_counter()
primes = sieve(num)
stopTime = time.perf_counter()

for i in primes:
    print(i, end=" ")
print()

print("Runtime %g secs" % (stopTime - startTime))

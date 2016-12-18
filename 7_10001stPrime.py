#!/bin/python
import sys

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

primes = primes_sieve(300000)

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print primes[n-1]

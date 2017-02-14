def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = {}

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes[i] = True

    return primes

def eulerFormula(n, a, b):
    return n**2 + a*n + b

primes = primes_sieve(10000)
n = int(raw_input())
maxCount = 0
# It generates the a elements: [-n:n]
for a in range(-n,n):
    # It generates the b elements:
    for b in primes:
        count = 0
        for k in xrange(n):
            num = eulerFormula(k, a, b)
            if num < 0 or (k**2 + k) % 2 == 0:
                pass
            if num in primes:
                count += 1
            else:
                if count > maxCount:
                    maxCount = count
                    bA = a
                    bB = b
                count = 0

print bA, bB
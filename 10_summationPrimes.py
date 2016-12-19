def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []
    summ = 0
    sum = []
    j = 1
    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        summ = summ + i
        sum.append(summ)
        primes.append(i)

    return sum, primes

sum, primes = primes_sieve(100);
print primes

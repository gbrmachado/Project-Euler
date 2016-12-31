import sys

def sumEvenFib(n):
    fib = [1,2]
    i = 2
    while (fib[i-1] + fib[i-2] <= n):
        fib.append(fib[i-1] + fib[i-2])
        i = i + 1

    return reduce(lambda x,y: x + y, filter(lambda x : x % 2 == 0, fib))

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    print(sumEvenFib(n))

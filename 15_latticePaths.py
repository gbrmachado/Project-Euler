d = {}

def countLatticePath(n,m):
    if (n,m) in d:
        return d[(n,m)]

    if n == 1: return 1 + m
    elif m == 1: return 1 + n

    else:
        d[(n,m)] = countLatticePath(n-1,m) + countLatticePath(n,m-1)
        return countLatticePath(n-1, m) + countLatticePath(n, m-1)


n = int(raw_input())
for i in xrange(n):
    n,m = map(int, raw_input().split(" "))
    print countLatticePath(n,m) % (pow(10,9) + 7)

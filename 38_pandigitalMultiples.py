# PanDigital Multiples

def isPanDigital(n, base):
    count = 0 
    d = {}
    for i in range(1,base):
        n2 = n * i
        while ( n2 > 0 and count < base ):
            num = n2 % 10
            if num in d or num == 0 or num > base:
                return False
            d[num] = True
            count += 1
            n2 /= 10

    return count == base

n, k = map(int, raw_input().split(" "))
for i in range(2, n):
    if isPanDigital(i, k):
        print i

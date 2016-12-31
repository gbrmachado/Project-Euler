def isSumOfNPower(n, p):
    sumP = 0
    j = n
    while j > 0:
        sumP += pow(j % 10, p)
        j /= 10
    return sumP == n

n = int(raw_input())
c = 0
for i in range(100, 600000):
    if isSumOfNPower(i, n):
        c += i
print c

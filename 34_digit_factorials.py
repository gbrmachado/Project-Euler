fat = {}
def fact(n):
    if n in fat:
        return fat[n]

    if n <= 1:
        return 1

    else:
        fatAux = n * fact(n-1)
        fat[n] = fatAux
        return fatAux

def getSumFactNums(n):
    sumDigits = 0
    while n > 0:
        sumDigits += fact(n % 10)
        n /= 10
    return sumDigits

n = int(raw_input())
count = 0
for i in range(10,n):
    if getSumFactNums(i) % i == 0:
        count += i
print count

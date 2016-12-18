# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    return reduce(lambda x, y: x * y, range(1,n+1), 1)

def sumElements(n):
    sum = 0
    while (n > 0):
        sum = sum + n % 10
        n = n/10
    return sum
n = int(raw_input())
for i in xrange(n):
    fact = int(raw_input())
    print sumElements(factorial(fact))

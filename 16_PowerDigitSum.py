# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
for i in xrange(n):
    num = pow(2,int(raw_input()))
    sumNumbers = 0
    while(num > 0):
        sumNumbers += num % 10
        num /= 10
    print sumNumbers

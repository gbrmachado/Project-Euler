memo = {1:1, 2:1}
# def fib(n):
#     if n in memo:
#         return memo[n]
#     else:
#         f = fib(n-1) + fib(n-2)
#         memo[n] = f
#         return f


def fib(n):
    for i in range(3,n+1):
        memo[i] = memo[i-2] + memo[i-1]
def nDigits(n):
    count = 0
    while n > 0:
        count += 1
        n = n/10
    return count

fib(100)
for i in memo:
    print memo[i]
# n = int(raw_input())
# j = 1
# while( nDigits(memo[j]) < n ):
#     j = j+1
# print j

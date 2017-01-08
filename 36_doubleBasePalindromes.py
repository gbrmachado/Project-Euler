# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPalindrome(n, base):
    num = n
    revBase = 0    
    while (num > 0):      
        digBase = num % base
        revBase = revBase * base + digBase
        
        num /= base
                
    return revBase == n

n, k = map(int, raw_input().split(" "))
summation = 0

for i in range(1,n):
    if isPalindrome(i,10) and isPalindrome(i, k):
        summation += i

print summation

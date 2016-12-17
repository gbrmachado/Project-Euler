#!/bin/python

import sys

def isPalindrone(x):
    if (x % 10 == 0):
        return False
    r = 0
    while (r < x):
        r = 10 * r + x % 10
        x = x/10

    return r == x or x == r/10

def generatePalindromes():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if isPalindrone(product):
                palindromes.append(product)

    return palindromes

def biggestPalindrome(l, n):    
    i = 0
    lenL = len(l)
    while (i < lenL and l[i] < n):
        i = i+1
    return l[i-1]
        
pals = generatePalindromes()
pals.sort()

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print biggestPalindrome(pals, n)


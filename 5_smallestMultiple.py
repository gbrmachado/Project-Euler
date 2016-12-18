#!/bin/python

import sys

def isEvenlyMultiple(x, n):
    for i in range(1,n+1):
        if x % i != 0:
            return False
    return True

def smallestMultiple(n):
    i = n
    while(not isEvenlyMultiple(i, n)):
        i = i + 1
        
    return i

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print smallestMultiple(n)

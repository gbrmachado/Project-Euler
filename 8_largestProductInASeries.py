#!/bin/python

import sys

def largestProduct(n, k):
    aux = map(int, list(str(n)))  #transform the number in a list of integers
    biggestMulti = -1
    for i in range(0, len(aux)-k):
        ist2 = aux[i:i+k]                      #sublist containing k elements
        mul = reduce(lambda x, y : x*y, ist2)  #product of elements of the list
        biggestMulti = max(biggestMulti, mul)

    return biggestMulti

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = raw_input().strip()
    print generateListKItens(num, k)

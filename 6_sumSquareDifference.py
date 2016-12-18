#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    squareOfSum = pow((n * (n+1)/2),2)

    sumOfSquares = (n * (n + 1) * (2*n + 1)) / 6
    print squareOfSum - sumOfSquares

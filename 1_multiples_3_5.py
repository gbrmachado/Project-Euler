#!/bin/python
import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    nM3 = (n-1) / 3
    sM3 = 3 * (nM3 * (nM3+1))/2

    nM5 = (n-1) / 5
    sM5 = 5 * (nM5 * (nM5+1))/2

    nM15 = (n-1) / 15
    sM15 = 15 * (nM15 * (nM15+1))/2

    print (sM3 + sM5 - sM15)

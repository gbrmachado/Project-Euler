#!/bin/python

import sys

grid = []
for x in xrange(3):
    grid.append([1]*26)

for grid_i in xrange(20):
    grid_temp = [1] * 23
    grid_temp[3:20] = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)

for x in xrange(3):
    grid.append([1]*26)

maxMult = 0
for i in range(3,23):
    for j in range(3,23):
        maxDown = maxLeft = maxDiagRight = 1
        for k in range(0,4):
            maxDown *= grid[i+k][j]
            maxLeft *= grid[i][j+k]
            maxDiagRight *= grid[i+k][j+k]

        maxMult = max(maxDown, maxLeft, maxDiagRight, maxMult)

print maxMult

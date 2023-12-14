#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def horizontal_reflection(pattern, middle):
    diff = 0
    for row in range(min(middle, len(pattern) - middle)):
        for (px1, px2) in zip(pattern[middle - row - 1], pattern[middle + row]):
            if px1 != px2:
                diff += 1
                if diff > 1:
                    return False
    return diff == 1

puzzle = [patterns.splitlines() for patterns in stdin.read().split('\n\n')]

ans = 0
for pattern in puzzle:
    found = False
    for row in range(1, len(pattern)):
        if horizontal_reflection(pattern, row):
            ans += 100 * row
            found = True
            break

    if found: continue

    transposed = list(zip(*pattern))
    for col in range(1, len(transposed)):
        if horizontal_reflection(transposed, col):
            ans += col
            break
print(ans)

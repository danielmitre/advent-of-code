#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def horizontal_reflection(pattern, middle):
    for row in range(min(middle, len(pattern) - middle)):
        if pattern[middle - row - 1] != pattern[middle + row]:
            return False
    return True

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

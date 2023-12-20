#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

readings = [[int(r) for r in line.split()] for line in stdin.readlines()]

largest = max(map(len, readings))
layers = [[0 for _ in range(largest)] for _ in range(largest)]

ans = 0
for reads in readings:
    size = len(reads)
    for i in range(size):
        layers[0][i] = reads[i]
        for level in range(1, i + 1):
            layers[level][i] = layers[level - 1][i] - layers[level - 1][i - 1]
    value = 0
    for i in range(size-1, 0, -1):
        value = layers[i][size - 1] + value
    ans += reads[size - 1] + value

print(ans)
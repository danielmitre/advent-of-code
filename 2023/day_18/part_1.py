#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import pairwise, batched
from sys import stdin

dir_mult = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

plan = [(dir_mult[dir], int(amount)) for dir, amount, _ in map(str.split, stdin.readlines())]

coords = [(x * amount, y * amount) for (x, y), amount in plan]

for prev, cur in pairwise(range(len(coords))):
    coords[cur] = (coords[cur][0] + coords[prev][0], coords[cur][1] + coords[prev][1])

area = 0
for cur, prev in pairwise(range(len(coords))):
    area += (coords[cur][0] * coords[prev][1] -  coords[prev][0] * coords[cur][1]) / 2

line_area = 1
for _, sz in plan:
    line_area += sz / 2

print(int(abs(area) + line_area))
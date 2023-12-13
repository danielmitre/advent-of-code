#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bisect import bisect

from sys import stdin

image = list(map(str.strip, stdin.readlines()))

galaxies = [(x, y) for x, row in enumerate(image) for y, pixel in enumerate(row) if pixel == '#']
empty_rows = [i for i in range(len(image)) if i not in {x for (x,_) in galaxies}]
empty_cols = [i for i in range(len(image[0])) if i not in {y for (_,y) in galaxies}]

print(sum(abs(x2 - x1) + abs(y2 - y1) + abs(bisect(empty_rows, x2) - bisect(empty_rows, x1)) + abs(bisect(empty_cols, y2) - bisect(empty_cols, y1)) for i, (x1, y1) in enumerate(galaxies) for j, (x2, y2) in enumerate(galaxies[i+1:])))

# dist = 0
# for i in range(len(galaxies)):
#     x1, y1 = galaxies[i]
#     for j in range(i + 1, len(galaxies)):
#         pairwise_dist = 0
#         x2, y2 = galaxies[j]
#         dist += abs(x2 - x1) \
#               + abs(y2 - y1) \
#               + abs(bisect(empty_rows, x2) - bisect(empty_rows, x1)) \
#               + abs(bisect(empty_cols, y2) - bisect(empty_cols, y1))
# print(dist)
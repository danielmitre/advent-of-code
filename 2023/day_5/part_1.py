#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

[_, [seeds], *maps] = [list(map(str.split, maps.split('\n\n')[0].strip().splitlines())) for maps in stdin.read().split(':')]
seeds = [int(s) for s in seeds]
maps = [sorted([[int(mmm) for mmm in mm] for mm in m]) for m in maps]

ans = float('inf')
for seed in seeds:
    cur = seed
    for mapping in maps:
        for [dest, source, size] in mapping:
            if source <= cur < source + size:
                cur = dest + (cur - source)
                break
    ans = min(ans, cur)
print(ans)
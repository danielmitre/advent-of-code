#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import partial
from collections import defaultdict

from sys import stdin, setrecursionlimit

setrecursionlimit(60000)

go_to = {
    '|': ((-1,  0), ( 1,  0)),
    '-': (( 0, -1), ( 0,  1)),
    'L': ((-1,  0), ( 0,  1)),
    'J': (( 0, -1), (-1,  0)),
    '7': (( 1,  0), ( 0, -1)),
    'F': (( 1,  0), ( 0,  1)),
    'S': ((-1,  0), ( 0,  1), ( 1,  0), ( 0, -1)),
    '.': Exception('whoops'),
}

connected = {
    (-1,  0): set('|7FS'), # north
    ( 0,  1): set('-J7S'), # east
    ( 1,  0): set('|LJS'), # south
    ( 0, -1): set('-LFS'), # west
    ( 0,  0): set('S'),    # initial position
}

def find_loop(start, curr, direction, tiles, visited = set()):
    x, y = curr

    if not(0 <= x < len(tiles)):
        return []
    
    if not(0 <= y < len(tiles[x])):
        return []

    if curr in visited:
        return []
    
    if tiles[x][y] not in connected[direction]:
        return []

    if curr == start:
        return [curr]

    visited.add(curr)
    ans = []

    for (_x, _y) in go_to[tiles[x][y]]:
        next_x, next_y = x + _x, y + _y
        branch = find_loop(start, (next_x, next_y), (_x, _y), tiles, visited)
        ans.append([curr] + branch)

    return max(ans, key=len)
    

tiles = list(map(str.strip, stdin.readlines()))

start_x, start_y = max((line.find('S'), i) for i, line in enumerate(tiles))[::-1]
print(max(len(find_loop((start_x, start_y), (start_x + dx, start_y + dy), (dx, dy), tiles))//2 for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0))))
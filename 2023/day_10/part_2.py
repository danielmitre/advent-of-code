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
    (-1,  0): set('|7FS'), # up
    ( 0,  1): set('-J7S'), # right
    ( 1,  0): set('|LJS'), # down
    ( 0, -1): set('-LFS'), # left
}

direction_name = {
    (-1,  0): '↑', # up
    ( 0,  1): '→', # right
    ( 1,  0): '↓', # down
    ( 0, -1): '←', # left
}

def find_loop(start, curr, direction, tiles, visited = set()):
    x, y = curr

    if not(0 <= x < len(tiles)) or not(0 <= y < len(tiles[x])):
        return []

    if tiles[x][y] not in connected[direction]:
        return []
    
    if curr in visited:
        return []

    if curr == start:
        return [(x, y, direction_name[direction])]

    visited.add(curr)

    ans = []
    for (_x, _y) in go_to[tiles[x][y]]:
        next_x, next_y = x + _x, y + _y
        ans.append([(x, y, direction_name[direction])] + find_loop(start, (next_x, next_y), (_x, _y), tiles, visited))
    return max(ans, key=len)
    

tiles = list(map(str.strip, stdin.readlines()))

start_x, start_y = max((line.find('S'), i) for i, line in enumerate(tiles))[::-1]
loop = max((find_loop((start_x, start_y), (start_x + dx, start_y + dy), (dx, dy), tiles) for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0))), key=len)
xray = [['.' for _ in line] for line in tiles]

for i in range(len(loop)):
    x, y, direction = loop[i]
    _, _, next_dir = loop[(i+1)%len(loop)]
    # This ensures the corners are represented
    # by its vertical direction
    if next_dir in '↓↑':
        direction = next_dir
    xray[x][y] = direction

for x in range(len(xray)):
    direction = None
    is_inside = False
    for y in range(len(xray[x])):
        if xray[x][y] != '.':
            if direction == None:
                direction = xray[x][y]
            is_inside = direction == xray[x][y]
            continue
        xray[x][y] = 'I' if is_inside else 'O'

print(sum(line.count('I') for line in xray))
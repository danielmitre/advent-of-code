#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
from collections import deque

DX = {
    '→':  0,
    '←':  0,
    '↑': -1,
    '↓':  1,
}
DY = {
    '→':  1,
    '←': -1,
    '↑':  0,
    '↓':  0,
}

MIRROR = {
    '/': {
        '→': '↑',
        '↑': '→',
        '↓': '←',
        '←': '↓',
    },
    '\\': {
        '→': '↓',
        '↓': '→',
        '↑': '←',
        '←': '↑',
    }
}

SPLITTER = {
    '|': {
        '→': '↑↓',
        '←': '↑↓',
        '↑': '↑',
        '↓': '↓',
    },
    '-': {
        '→': '→',
        '←': '←',
        '↑': '←→',
        '↓': '←→',
    }
}

layout = [line.strip() for line in stdin.readlines()]

def energise(start_pos, start_dir) -> int:
    q = deque()
    q.append((start_pos, start_dir))

    visited = set()
    while len(q):
        cur = q.popleft()
        (x, y), dir = cur

        if cur in visited:
            continue
        if x < 0 or x >= len(layout):
            continue
        if y < 0 or y >= len(layout[0]):
            continue

        visited.add(cur)
        pixel = layout[x][y]
        if pixel == '.':
            new_x, new_y = x + DX[dir], y + DY[dir]
            q.append(((new_x, new_y), dir))
            continue
        if pixel in '/\\':
            new_dir = MIRROR[pixel][dir]
            new_x, new_y = x + DX[new_dir], y + DY[new_dir]
            q.append(((new_x, new_y), new_dir))
            continue
        if pixel in '-|':
            for new_dir in SPLITTER[pixel][dir]:
                new_x, new_y = x + DX[new_dir], y + DY[new_dir]
                q.append(((new_x, new_y), new_dir))

    return len({(x, y) for (x, y), _ in visited})

rows, cols = len(layout), len(layout[0])

print(max(
    *(energise((x, 0), '→') for x in range(rows)),
    *(energise((0, y), '↓') for y in range(cols)),
    *(energise((x, len(layout[0]) - 1), '←') for x in range(rows)),
    *(energise((len(layout) - 1, y), '↑') for y in range(cols)),
))

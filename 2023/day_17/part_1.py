#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
from sys import stdin

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

TURNS = {
    '→': '↑↓',
    '←': '↑↓',
    '↑': '←→',
    '↓': '←→',
}

def in_bounds(pos, heatmap) -> bool:
    x, y = pos
    if x < 0 or x >= len(heatmap):
        return False
    if y < 0 or y >= len(heatmap[0]):
        return False
    return True

def dijkstra(dest, heatmap):
    # dir counter, dir, pos
    vis = set()

    pq = []
    heapq.heappush(pq, (0, 0, '↓', (0, 0)))

    while pq:
        dist, dir_cnt, dir, pos = heapq.heappop(pq)
        x, y = pos

        if pos == dest:
            return dist

        if ((dir_cnt, dir, pos) in vis):
            continue

        vis.add((dir_cnt, dir, pos))
        
        if dir_cnt < 3:
            new_x, new_y = x + DX[dir], y + DY[dir]
            if in_bounds((new_x, new_y), heatmap):
                heapq.heappush(pq, (dist + heatmap[new_x][new_y], dir_cnt + 1, dir, (new_x, new_y)))
        
        for new_dir in TURNS[dir]:
            new_x, new_y = x + DX[new_dir], y + DY[new_dir]
            if in_bounds((new_x, new_y), heatmap):
                heapq.heappush(pq, (dist + heatmap[new_x][new_y], 1, new_dir, (new_x, new_y)))
    
    return float('inf')

heatmap = [list(map(int, line.strip())) for line in stdin.readlines()]
print(dijkstra((len(heatmap) - 1, len(heatmap[0]) - 1), heatmap))

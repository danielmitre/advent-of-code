#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
from sys import stdin

DX = { '→':  0, '←':  0, '↑': -1, '↓':  1 }
DY = { '→':  1, '←': -1, '↑':  0, '↓':  0 }
TURNS = { '→': '↑↓', '←': '↑↓', '↑': '←→', '↓': '←→' }

def in_bounds(pos, heatmap) -> bool:
    if not 0 <= pos[0] < len(heatmap):
        return False
    return 0 <= pos[1] < len(heatmap[0])

def dijkstra(dest, heatmap):
    vis = set() # streak, dir, pos
    pq = [] # dist, streak, dir, pos
    heapq.heappush(pq, (0, 0, '↓', (0, 0)))
    heapq.heappush(pq, (0, 0, '→', (0, 0)))

    while pq:
        dist, dir_cnt, dir, pos = heapq.heappop(pq)
        x, y = pos

        if not in_bounds(pos, heatmap):
            continue

        dist += heatmap[x][y]        
        
        if pos == dest and dir_cnt >= 4:
            return dist

        if ((dir_cnt, dir, pos) in vis):
            continue

        vis.add((dir_cnt, dir, pos))

        if dir_cnt < 10:
            heapq.heappush(pq, (dist, dir_cnt + 1, dir, (x + DX[dir], y + DY[dir])))
        
        if dir_cnt >= 4:
            for new_dir in TURNS[dir]:
                heapq.heappush(pq, (dist, 1, new_dir, (x + DX[new_dir], y + DY[new_dir])))
    
    return float('inf')

heatmap = [list(map(int, line.strip())) for line in stdin.readlines()]
print(dijkstra((len(heatmap) - 1, len(heatmap[0]) - 1), heatmap) - heatmap[0][0])

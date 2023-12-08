#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
from queue import Queue

[_, [seeds], *maps] = [list(map(str.split, maps.split('\n\n')[0].strip().splitlines())) for maps in stdin.read().split(':')]
seeds = [(int(seeds[i]), int(seeds[i])+int(seeds[i+1])-1) for i in range(0, len(seeds), 2)]
maps = [sorted([[int(source), int(source)+int(size)-1, int(dest), int(dest)+int(size)-1] for [dest, source, size] in m]) for m in maps]

ans = float('inf')
fifo = Queue()
for [left, right] in seeds:
    fifo.put([left, right])

for (i, mapping) in enumerate(maps):
    new_fifo = Queue()
    while not fifo.empty():
        left, right = fifo.get()
        intersected = False

        for [source_left, source_right, dest_left, dest_right] in mapping:
            if right < source_left:
                continue

            if left > source_right:
                continue

            intersected = True
            intersection = [max(left, source_left), min(right, source_right)]
            offset = intersection[0] - source_left
            intersection_size = intersection[1] - intersection[0]

            new_fifo.put([dest_left + offset, dest_left + offset + intersection_size])

            if left < source_left:
                fifo.put([left, source_left - 1])

            if right >= source_right:
                fifo.put([source_right + 1, right])
        
        if not intersected:
            new_fifo.put([left, right])

    fifo = new_fifo

while not fifo.empty():
    ans = min(ans, fifo.get()[0])
print(ans)
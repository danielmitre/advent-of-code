#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

schematic = list(map(str.strip, stdin.readlines()))
colors = []
gears = []
numbers = {}
cur_color = 1
for row in range(len(schematic)):
    colors.append([])
    for col in range(len(schematic[row])):
        ch = schematic[row][col]

        if ch.isdigit():
            colors[row].append(cur_color)
            numbers[cur_color] = numbers.get(cur_color, 0) * 10 + int(ch)

        elif ch == '*':
            colors[row].append(0)
            gears.append((row, col))
            cur_color += 1

        else:
            colors[row].append(0)
            cur_color += 1

ans = 0
for (row, col) in gears:
    neighbors = set()
    for _row in [-1, 0, 1]:
        for _col in [-1, 0, 1]:
            r = min(max(row + _row, 0), len(schematic) - 1)
            c = min(max(col + _col, 0), len(schematic[r]) - 1)
            neighbors.add(colors[r][c])
    neighbors.remove(0)
    
    if len(neighbors) != 2:
        continue

    ratio = 1
    for color in neighbors:
        ratio *= numbers[color]
    ans += ratio

print(ans)
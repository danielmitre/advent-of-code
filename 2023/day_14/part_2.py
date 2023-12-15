#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def tilt_north(puzzle):
    for row in range(len(puzzle[0])):
        free = 0
        for line in range(len(puzzle)):
            if puzzle[line][row] == '#':
                free = line + 1
            if puzzle[line][row] == 'O':
                puzzle[line][row], puzzle[free][row] = puzzle[free][row], puzzle[line][row]
                free += 1

def tilt_south(puzzle):
    for row in range(len(puzzle[0])):
        free = len(puzzle)-1
        for line in range(len(puzzle)-1, -1, -1):
            if puzzle[line][row] == '#':
                free = line - 1
            if puzzle[line][row] == 'O':
                puzzle[line][row], puzzle[free][row] = puzzle[free][row], puzzle[line][row]
                free -= 1

def tilt_west(puzzle):
    for line in range(len(puzzle)):
        free = 0
        for row in range(len(puzzle[0])):
            if puzzle[line][row] == '#':
                free = row + 1
            if puzzle[line][row] == 'O':
                puzzle[line][row], puzzle[line][free] = puzzle[line][free], puzzle[line][row]
                free += 1

def tilt_east(puzzle):
    for line in range(len(puzzle)):
        free = len(puzzle[0])-1
        for row in range(len(puzzle[0])-1, -1, -1):
            if puzzle[line][row] == '#':
                free = row - 1
            if puzzle[line][row] == 'O':
                puzzle[line][row], puzzle[line][free] = puzzle[line][free], puzzle[line][row]
                free -= 1

def north_load(puzzle):
    load = 0
    for i, line in enumerate(puzzle):
        for cell in line:
            if cell == 'O':
                load += len(puzzle) - i
    return load

puzzle = [list(patterns.strip()) for patterns in stdin]

memo = {}
cycle = 0
while (cycle := cycle + 1) <= 1_000_000_000:
    tilt_north(puzzle)
    tilt_west(puzzle)
    tilt_south(puzzle)
    tilt_east(puzzle)

    key = tuple(tuple(x) for x in puzzle)
    if key in memo:
        remaining = 1_000_000_000 - cycle
        loop_size = cycle - memo[key]
        cycle = cycle + (remaining // loop_size) * loop_size
    memo[key] = cycle

print(north_load(puzzle))
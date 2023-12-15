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

def north_load(puzzle):
    load = 0
    for i, line in enumerate(puzzle):
        for cell in line:
            if cell == 'O':
                load += len(puzzle) - i
    return load

puzzle = [list(patterns.strip()) for patterns in stdin]

tilt_north(puzzle)
print(north_load(puzzle))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
import re

print(sum(map(lambda game: game[0] if game[1] else 0, ([int(next(re.finditer(r'Game (\d+):', line)).group(1)), all(map(lambda round: all(map(lambda marble: int(marble[0]) <= {'red': 12, 'green': 13, 'blue': 14}[marble[1]], round)), (map(str.split, round.split(', ')) for round in map(str.strip, line.split(':')[1].split(';')))))] for line in stdin.readlines()))))
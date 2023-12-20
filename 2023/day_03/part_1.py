#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

ans = 0
schematic = list(map(str.strip, stdin.readlines()))
for row in range(len(schematic)):
    number = '0'
    symbol = False
    for col in range(len(schematic[row])):
        ch = schematic[row][col]
        if not ch.isdigit():
            if symbol:
                ans += int(number)
            number = '0'
            symbol = False
            continue

        number += ch
        for _row in [-1, 0, 1]:
            for _col in [-1, 0, 1]:
                r = min(max(row + _row, 0), len(schematic) - 1)
                c = min(max(col + _col, 0), len(schematic[r]) - 1)
                if schematic[r][c] != '.' and not schematic[r][c].isdigit():
                    symbol = True
    if symbol:
        ans += int(number)

print(ans)



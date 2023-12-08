#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from sys import stdin

directions, _, *maps = map(str.strip, stdin.readlines())
maps = {node: {'L': left, 'R': right} for (node, left, right) in (re.findall(r'(.*) = \((.*), (.*)\)', node)[0] for node in maps)}

cur = 'AAA'
steps = 0
while cur != 'ZZZ':
    cur = maps[cur][directions[steps % len(directions)]]
    steps += 1

print(steps)
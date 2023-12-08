#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import lcm
import re
import sys

directions, _, *maps = map(str.strip, sys.stdin.readlines())
maps = {node: {'L': left, 'R': right} for (node, left, right) in (re.findall(r'(.*) = \((.*), (.*)\)', node)[0] for node in maps)}

def dist_to_z(node):
    steps = 0
    while node[-1] != 'Z':
        node = maps[node][directions[steps % len(directions)]]
        steps += 1
    return steps

print(lcm(*(dist_to_z(node) for node in filter(lambda node: node[-1] == 'A', maps.keys()))))
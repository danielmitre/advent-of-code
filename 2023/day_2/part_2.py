#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
import re

from sys import stdin

print(sum(map(lambda game: game['red'] * game['green'] * game['blue'], (reduce(lambda acum, cur: {**acum, cur[1]: max(acum.get(cur[1], 0), int(cur[0]))}, line, {}) for line in [map(str.split, map(str.strip, re.split(r';|, ', line.split(':')[1]))) for line in stdin.readlines()]))))
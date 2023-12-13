#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache
from sys import stdin

@lru_cache(maxsize=None)
def arrangements(record, i, cur_group, groups):
    if i == len(record):
        return cur_group == len(groups)
    
    ans = 0
    if record[i] in '.?':
        ans += arrangements(record, i + 1, cur_group, groups)

    if record[i] in '#?' and cur_group < len(groups):
        if not all(map(set('#?').__contains__, record[i:i+groups[cur_group]])):
            return ans
        if i + groups[cur_group] > len(record):
            return ans
        if i + groups[cur_group] == len(record):
            return ans + arrangements(record, i + groups[cur_group], cur_group + 1, groups)
        if record[i + groups[cur_group]] not in '?.':
            return 0 + ans
        return ans + arrangements(record, i + groups[cur_group] + 1, cur_group + 1, groups)
    return ans

print(sum(arrangements(record, 0, 0, groups) for (record, groups) in [('?'.join((line.split()[0] for _ in range(5))), 5 * tuple(map(int,line.split()[1].split(',')))) for line in stdin.readlines()]))

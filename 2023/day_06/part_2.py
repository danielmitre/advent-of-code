#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

time, distance = [int(''.join(race.split()[1:])) for race in stdin.readlines()]

def lower_bound(time, distance):
    lo = 0
    hi = time
    ans = 0
    while (lo <= hi):
        mid = (lo + hi) // 2
        if (time - mid) * mid > distance:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

def upper_bound(time, distance):
    lo = 0
    hi = time
    ans = 0
    while (lo <= hi):
        mid = (lo + hi) // 2
        if (time - mid) * mid > distance:
            lo = mid + 1
            ans = mid
        else:
            hi = mid - 1
    return ans

print(upper_bound(time, distance) - lower_bound(time, distance) + 1)
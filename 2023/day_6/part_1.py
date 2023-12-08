#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

times, distances = [list(map(int, race.split()[1:])) for race in stdin.readlines()]

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

ans = 1
for i in range(len(times)):
    time, distance = times[i], distances[i]
    half = time // 2
    if (half * (time - half)) <= distance:
        ans = 0
        break
    lo = lower_bound(time, distance)
    hi = upper_bound(time, distance)
    ans *= hi - lo + 1
print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

def HASH(seq: str) -> int:
    value = 0
    for ch in seq:
        value = ((value + ord(ch)) * 17) % 256
    return value

print(sum(HASH(seq) for seq in stdin.read().strip().split(',')))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from sys import stdin

def cmp(cards):
    order = 'AKQJT98765432'[::-1]
    hand, _ = cards
    return sorted(Counter(hand).values(), reverse=True), list(map(order.index, hand))

print(sum(int(bid) * i for i, (_, bid) in enumerate(sorted(map(str.split, stdin.readlines()), key=cmp), 1)))

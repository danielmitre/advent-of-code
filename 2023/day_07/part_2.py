#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from sys import stdin

def cmp(cards):
    order = 'AKQT98765432J'[::-1]
    hand, _ = cards
    c = Counter(hand)
    jokers = c.pop('J', 0)
    freq = sorted(c.values() or [0], reverse=True)
    freq[0] += jokers
    return freq, list(map(order.index, hand))

print(sum(int(bid) * i for i, (_, bid) in enumerate(sorted(map(str.split, stdin.readlines()), key=cmp), 1)))

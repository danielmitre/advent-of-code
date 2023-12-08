#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from functools import cmp_to_key
from sys import stdin

def cmp(left, right):
    card = 'AKQJT98765432'
    hand_l, _, counter_l = left
    hand_r, _, counter_r = right

    if len(counter_l) == len(counter_r):
        if counter_r[0][1] == counter_l[0][1]:
            return -1 if list(map(card.index, hand_l)) < list(map(card.index, hand_r)) else 1
        return counter_r[0][1] - counter_l[0][1]
    return len(counter_l) - len(counter_r)

print(sum(bid * i for i, (_, bid, _) in enumerate(sorted(((hand, int(bid), Counter(hand).most_common()) for (hand, bid) in map(str.split, stdin.readlines())), key=cmp_to_key(cmp), reverse=True), 1)))


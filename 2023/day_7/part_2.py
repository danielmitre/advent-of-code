#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from functools import cmp_to_key
from sys import stdin

def cmp(left, right):
    card = 'AKQT98765432J'
    hand_l, _, counter_l = left
    hand_r, _, counter_r = right
    joker_l, joker_r = counter_l['J'], counter_r['J']
    counter_r -= Counter({'J': joker_r})
    counter_r += Counter({counter_r.most_common()[0][0] if len(counter_r.most_common()) else 'J': joker_r})
    counter_l -= Counter({'J': joker_l})
    counter_l += Counter({counter_l.most_common()[0][0] if len(counter_l.most_common()) else 'J': joker_l})
    
    if len(counter_l) == len(counter_r):
        if counter_r.most_common()[0][1] == counter_l.most_common()[0][1]:
            return -1 if list(map(card.index, hand_l)) < list(map(card.index, hand_r)) else 1
        return counter_r.most_common()[0][1] - counter_l.most_common()[0][1]
    return len(counter_l) - len(counter_r)

print(sum(bid * i for i, (_, bid, _) in enumerate(sorted(((hand, int(bid), Counter(hand)) for (hand, bid) in map(str.split, stdin.readlines())), key=cmp_to_key(cmp), reverse=True), 1)))
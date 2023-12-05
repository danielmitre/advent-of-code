#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

cards = [len(set.intersection(*(set(x.split()) for x in card.split(':')[1].split('|')))) for card in stdin.readlines()]

for i in range(len(cards)-1, -1, -1):
    cards[i] += sum(cards[i + 1 : i + 1 + cards[i]])

print(sum(cards) + len(cards))
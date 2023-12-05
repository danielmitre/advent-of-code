#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

print(sum(int(2**(len(set.intersection(*(set(x.split()) for x in card.split(':')[1].split('|'))))-1)) for card in stdin.readlines()))
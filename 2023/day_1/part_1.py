#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin

print(sum((int(''.join((next(filter(str.isdigit, line)), next(filter(str.isdigit, reversed(line)))))) for line in stdin.readlines())))
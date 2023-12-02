#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin
import re

pattern = re.compile(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))')
value = {
    **{str(i): str(i) for i in range(10)},
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

print(sum(map(int, list(''.join((value[re.findall(pattern, line)[0]], value[re.findall(pattern, line)[-1]])) for line in stdin.readlines()))))
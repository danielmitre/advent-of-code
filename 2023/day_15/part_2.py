#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import defaultdict
from sys import stdin

def HASH(seq: str) -> int:
    value = 0
    for ch in seq:
        value = ((value + ord(ch)) * 17) % 256
    return value

def dash(label: str, boxes: defaultdict):
    '''
    Go to the relevant box and remove the lens
    with the given label if it is present in the box.

    Then, move any remaining lenses as far forward
    in the box as they can go without changing their order,
    filling any space made by removing the indicated lens.

    If no lens in that box has the given label, nothing happens.
    '''
    idx = HASH(label)
    boxes[idx] = [(_label, _len) for (_label, _len) in boxes[idx] if _label != label]

def equal(label: str, focal: int, boxes: defaultdict):
    '''
    If there is already a lens in the box with the same label,
    replace the old lens with the new lens:
    remove the old lens and put the new lens in its place,
    not moving any other lenses in the box.
    
    If there is not already a lens in the box with the same label,
    add the lens to the box immediately behind any lenses already in the box.
    Don't move any of the other lenses when you do this.
    If there aren't any lenses in the box,
    the new lens goes all the way to the front of the box.
    '''
    idx = HASH(label)
    found = any(map(lambda x: x[0] == label, boxes[idx]))
    if found:
        boxes[idx] = [(_label, _len if _label != label else focal) for (_label, _len) in boxes[idx]]
    else:
        boxes[idx].append((label, focal))

def HASHMAP(boxes: defaultdict, *args):
    if args[1] == '':
        dash(args[0], boxes)
    else:
        equal(args[0], int(args[1]), boxes)
    return HASH(args[0])

def focusing_power(init_seq) -> int:
    boxes = defaultdict(list)
    for seq in init_seq:
        HASHMAP(boxes, *re.split(r'[-=]', seq))
    power = 0
    for box in range(256):
        for i, (label, focal) in enumerate(boxes[box], 1):
            power += (box + 1) * i * focal
        
    return power

print(focusing_power(stdin.read().strip().split(',')))
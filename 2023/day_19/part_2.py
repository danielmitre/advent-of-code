#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from sys import stdin

def gt(elements, key, threshold: int):
    left, right = dict(elements), dict(elements)
    left[key] = {x for x in elements[key] if x > threshold}
    right[key] = {x for x in elements[key] if x <= threshold}
    return (left, right)

def lt(elements, key, threshold: int):
    left, right = dict(elements), dict(elements)
    left[key] = {x for x in elements[key] if x < threshold}
    right[key] = {x for x in elements[key] if x >= threshold}
    return (left, right)

def parse_workflow(wf):
    name, expr = re.findall(r'(.*)\{(.*)\}', wf)[0]
    rules = []
    for rule in expr.split(','):
        if ':' not in rule:
            rules.append((gt, 'x', -1, rule))   # "> -1" to always yield True
            continue
        condition, next_wf = rule.split(':')
        var, op, value = re.findall(r'(.*)([><])(.*)', condition)[0]
        op = {'>': gt, '<': lt}[op]
        rules.append((op, var, int(value), next_wf))
    return name, rules

def parse_rating(rating):
    return {k: int(v) for (k, v) in re.findall(r'([a-zA-Z])=(\d*)', rating)}

def run_workflows(rating, current, idx, workflows):
    if current == 'A':
        return [rating]
    if current == 'R' or idx >= len(workflows[current]):
        return [{'x': set(), 'm': set(), 'a': set(), 's': set()}]
    
    op, var, value, next_wf = workflows[current][idx]
    left, right = op(rating, var, value)
    return [*run_workflows(left, next_wf, 0, workflows), *run_workflows(right, current, idx + 1, workflows)]

_w, _r = stdin.read().split('\n\n')

workflows = {name: rules for (name, rules) in map(parse_workflow, _w.splitlines())}
valids = run_workflows({'x': set(range(1, 4001)), 'm': set(range(1, 4001)), 'a': set(range(1, 4001)), 's': set(range(1, 4001))}, 'in', 0, workflows)

ans = 0
for valid in valids:
    combinations = 1
    for v in valid.values():
        combinations *= len(v)
    ans += combinations
print(ans)
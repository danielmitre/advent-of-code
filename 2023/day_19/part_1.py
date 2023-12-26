#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from sys import stdin

def parse_workflow(wf):
    name, expr = re.findall(r'(.*)\{(.*)\}', wf)[0]
    rules = []
    for rule in expr.split(','):
        if ':' not in rule:
            rules.append((int.__gt__, 'x', -1, rule))   # "> -1" to always yield True
            continue
        condition, next_wf = rule.split(':')
        var, op, value = re.findall(r'(.*)([><])(.*)', condition)[0]
        op = {'>': int.__gt__, '<': int.__lt__}[op]
        rules.append((op, var, int(value), next_wf))
    return name, rules

def parse_rating(rating):
    return {k: int(v) for (k, v) in re.findall(r'([a-zA-Z])=(\d*)', rating)}

def run_workflows(rating):
    current = 'in'
    path = ['in']
    while current not in ('A', 'R'):
        for (op, var, value, next_wf) in workflows[current]:
            if op(rating[var], value):
                current = next_wf
                path.append(current)
                break
    print(rating, path)
    return {'R': 0, 'A': sum(rating.values())}[current]

_w, _r = stdin.read().split('\n\n')

workflows = {name: rules for (name, rules) in map(parse_workflow, _w.splitlines())}

print(sum(map(run_workflows, map(parse_rating, _r.splitlines()))))
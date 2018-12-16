#!/usr/bin/env python3

import string
from operator import itemgetter


with open("input5.txt") as f:
    polymer = next(f).rstrip()


def remove_unit(polymer, unit):
    return [ u for u in polymer if u.lower() != unit ]


def remove_reactions(polymer):
    stack = []

    for right in polymer:
        if not stack:
            stack.append(right)
            continue

        left = stack[-1]

        if left.lower() != right.lower() or left == right:
            stack.append(right)
            continue

        stack.pop()

    return stack


def find_shortest_polymer(polymer):
    polymers = [
        (unit, len(remove_reactions(remove_unit(polymer, unit))))
            for unit in string.ascii_lowercase
    ]

    return min(polymers, key=itemgetter(1))[1]


polymer_1 = remove_reactions(polymer)

print("solution 1:", len(polymer_1))

polymer_2 = find_shortest_polymer(polymer)

print("solution 2:", polymer_2)

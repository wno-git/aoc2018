#!/usr/bin/env python3

with open("input5.txt") as f:
    polymer = next(f).rstrip()


# This is O(n^2) and very slow. New lists are created on every iteration
# requiring a O(n) memory copy.
# There is probably a much better way...

def remove_reaction(polymer):
    assert len(polymer) > 1

    for i in range(0, len(polymer) - 1):
        a = polymer[i]
        b = polymer[i + 1]

        if a == b:
            # no reaction
            continue

        if a.lower() == b.lower():
            # opposite polarities, reaction
            return polymer[:i] + polymer[i + 2:]

    return polymer


while True:
    p = remove_reaction(polymer)
    if p == polymer:
        # no more reactions
        break

    polymer = p


print("solution:", len(polymer))

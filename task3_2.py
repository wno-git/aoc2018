#!/usr/bin/env python3

import re

re_claim = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

class Claim(object):
    def __init__(self, no, x, y, w, h):
        self.no = no
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return "id={}".format(self.no)


def get_claim(line):
    r = re_claim.match(line)
    claim = Claim(
        int(r.group(1)),
        int(r.group(2)),
        int(r.group(3)),
        int(r.group(4)),
        int(r.group(5)))

    return claim


with open("input3_1.txt") as f:
    claims = list(map(get_claim, f))


def build_fabric(claims):
    fabric = [0] * 1000 * 1000

    for claim in claims:
        for y in range(claim.y, claim.y + claim.h):
            for x in range(claim.x, claim.x + claim.w):
                fabric[y * 1000 + x] = fabric[y * 1000 + x] + 1

    return fabric


def has_overlap(fabric, claim):
    for y in range(claim.y, claim.y + claim.h):
        for x in range(claim.x, claim.x + claim.w):
            if fabric[y * 1000 + x] > 1:
                return True

    return False


def find_nonoverlapping_claim(fabric, claims):
    claim = list(filter(lambda c: not has_overlap(fabric, c), claims))

    assert len(claim) == 1

    return claim[0]

fabric = build_fabric(claims)

claim = find_nonoverlapping_claim(fabric, claims)

print("non-overlapping claim:", claim)

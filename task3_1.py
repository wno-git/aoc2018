#!/usr/bin/env python3

import re

re_claim = re.compile(".* ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")


def get_claim(line):
    r = re_claim.match(line)
    x = int(r.group(1))
    y = int(r.group(2))
    w = int(r.group(3))
    h = int(r.group(4))

    return (x, y, w, h)


with open("input3_1.txt") as f:
    claims = list(map(get_claim, f))


fabric = [0] * 1000 * 1000

for claim in claims:
    claimx = claim[0]
    claimy = claim[1]
    claimw = claim[2]
    claimh = claim[3]
    for y in range(claimy, claimy + claimh):
        for x in range(claimx, claimx + claimw):
            fabric[y * 1000 + x] = fabric[y * 1000 + x] + 1


claimed = len(list(filter(lambda x: True if x > 1 else False, fabric)))

print(claimed)

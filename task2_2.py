#!/usr/bin/env python3

with open("input2_1.txt") as f:
    boxids = list(map(lambda x: x.rstrip(), f))


def get_differing_position(a, b):
    assert len(a) == len(b)

    n_diff = 0
    pos = -1
    for i in range(0, len(a)):
        if a[i] == b[i]:
            continue
        else:
            n_diff = n_diff + 1
            pos = i

    if n_diff == 0:
        # no difference
        return (False, -1)
    elif n_diff == 1:
        # one difference
        return (True, pos)
    else:
        # many differences
        return (False, -1)


testids1 = [
    "raba",
    "acbb",
    "vzza",
    "avbb",
    "erra",
]

#boxids = testids1

# this is O(n^2) :/
# there could be a better way with proper fuzzy string matching algorithms
boxid = None
diff_pos = None
for i in range(0, len(boxids)):
    for j in range(0, len(boxids)):
        found, pos = get_differing_position(boxids[i], boxids[j])
        if found:
            boxid = i
            diff_pos = pos
            break

print("id:", boxid, "difference at:", diff_pos)
print("common:", boxids[boxid][:diff_pos] + boxids[boxid][diff_pos+1:])

#!/usr/bin/env python3

with open("input2_1.txt") as f:
    boxids = list(map(lambda x: x.rstrip(), f))


def get_letter_counts(boxid):
    letter_counts = dict()

    for i in range(0, len(boxid)):
        letter = boxid[i]
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    return letter_counts

def has_exactly_n(boxid, n):
    letter_counts = get_letter_counts(boxid)

    n_counts = { k: v for k, v in letter_counts.items() if v == n }

    if n_counts:
        return True
    else:
        return False

testid1 = "abbcccdddda"
testid2 = "abbbcccddddaa"
testid3 = "abbccdda"

#print(get_letter_counts(testid))
#print(has_exactly_n(testid1, 2))
#print(has_exactly_n(testid1, 3))
#print(has_exactly_n(testid2, 2))
#print(has_exactly_n(testid3, 3))

# gief currying :(
def has_exactly_two(boxid):
    return 1 if has_exactly_n(boxid, 2) else 0

def has_exactly_three(boxid):
    return 1 if has_exactly_n(boxid, 3) else 0

have_exactly_twos = sum(map(has_exactly_two, boxids))
have_exactly_threes = sum(map(has_exactly_three, boxids))

print(have_exactly_twos)
print(have_exactly_threes)

print("cksum:", have_exactly_twos * have_exactly_threes)

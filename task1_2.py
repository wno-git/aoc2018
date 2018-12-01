#!/usr/bin/env python3

cl_test1 = [1, -1]
cl_test2 = [3, 3, 4, -2, -4]

with open("input1_1.txt") as f:
    cl = list(map(int, f))

#cl = cl_test2

freqs = set([0])
i = 0
freq = 0

while True:
    freq = freq + cl[i]

    if freq in freqs:
        print("freq seen:", freq)
        break
    else:
        freqs.add(freq)

    i = (i + 1) % len(cl)

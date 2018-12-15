#!/usr/bin/env python3

from functools import reduce
from itertools import groupby
import re

re_wake = re.compile(".*:([0-9]+)\] wakes")
re_sleep = re.compile(".*:([0-9]+)\] falls")
re_begin = re.compile(".*#([0-9]+)")

with open("input4_1.txt") as f:
    events = sorted(f)


def get_begin_event(event):
    m = re_begin.match(event)
    return (True, int(m.group(1))) if m else (False, None)


def get_wake_event(event):
    m = re_wake.match(event)
    return (True, int(m.group(1))) if m else (False, None)


def get_sleep_event(event):
    m = re_sleep.match(event)
    return (True, int(m.group(1))) if m else (False, None)


def make_sleep(start, end):
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert not start < 0 and start < end

    return [
        1 if start <= x and x < end else 0 for x in range(0, 60)
    ]


def get_sleeps(events):
    sleeps = []
    current_guard = None
    sleep_start = None

    for event in events:
        begin = get_begin_event(event)
        if begin[0]:
            current_guard = begin[1]
            continue

        sleep = get_sleep_event(event)
        if sleep[0]:
            sleep_start = sleep[1]
            continue

        wake = get_wake_event(event)
        if wake[0]:
            sleep_end = wake[1]
            sleeps.append(
                (current_guard, make_sleep(sleep_start, sleep_end)))
            continue

        assert False

    return sleeps


def kv_guard_id(kv):
    return kv[0]


def kv_sleep(kv):
    return kv[1]


def get_guard_sleep_totals(sleeps):
    assert isinstance(sleeps, list)

    sleeps = sorted(sleeps, key=kv_guard_id)

    add_sleeps = lambda a, b: [ sum(x) for x in zip(a, b) ]

    # this is basically a reduce-by-key
    totals = [
        (guard, reduce(add_sleeps, map(kv_sleep, guard_sleeps)))
            for guard, guard_sleeps in
                groupby(sleeps, key=kv_guard_id)
    ]

    return totals


def get_sleep_stats(sleep):
    assert isinstance(sleep, list)

    most_slept = sorted(sleep, reverse=True)[0]
    most_slept_minute = sleep.index(most_slept)
    total_sleep = sum(sleep)

    return (total_sleep, most_slept_minute)


def get_guard_stats(guard_totals):
    return [
            (kv_guard_id(kv), get_sleep_stats(kv_sleep(kv))) for
            kv in guard_totals
    ]


def get_most_sleeper(guard_stats):
    kv_stats_sleep_total = lambda x: x[1][0]
    return sorted(guard_stats, key=kv_stats_sleep_total, reverse=True)[0]


sleeps = get_sleeps(events)

guard_sleep_totals = get_guard_sleep_totals(sleeps)

guard_stats = get_guard_stats(guard_sleep_totals)

most_sleeper = get_most_sleeper(guard_stats)

solution = kv_guard_id(most_sleeper) * most_sleeper[1][1]

print("solution:", solution)

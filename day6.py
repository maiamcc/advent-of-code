#! /usr/bin/env python
from collections import defaultdict

from utils import read_file

### PART ONE
print('---PART ONE---')
inp = read_file('input/input6', sep='\n\n')


def qs_with_any_yes(grp: str) -> int:
    return len(set([ch for ch in grp if ch.isalpha()]))


print(sum([qs_with_any_yes(grp) for grp in inp]))


### PART TWO
print('---PART TWO---')


def qs_with_all_yes(grp: str) -> int:
    rows = grp.split()
    counts = defaultdict(int)
    for row in rows:
        for ch in row:
            counts[ch] += 1

    return len([k for k, v in counts.items() if v == len(rows)])


print(sum([qs_with_all_yes(grp) for grp in inp]))


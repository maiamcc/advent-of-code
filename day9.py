#! /usr/bin/env python
from collections import defaultdict
from typing import List

from utils import read_file


### PART ONE
print('---PART ONE---')
inp = read_file('input/input9', typ=int)


# lol I stole this from day 1
def twosum(li: List[int], targ: int, elem_counts=None):
    if elem_counts is None:
        elem_counts = defaultdict(int)
        for elem in li:
            elem_counts[elem] += 1

    for elem in li:
        if targ-elem in elem_counts and (elem != targ-elem or elem_counts[elem] >= 2):
            return elem, targ-elem

    return None


def has_twosum(li: List[int], targ: int) -> bool:
    return bool(twosum(li, targ))


def find_first_bad_number(numbers: List[int]) -> int:
    i = 25  # start after the preamble
    while i < len(numbers):
        if not has_twosum(numbers[i-25:i], numbers[i]):
            # NOT the sum of two numbers within the last 25 elems
            return numbers[i]
        i += 1
    raise Exception('well fuck')


bad_num = find_first_bad_number(inp)
print(bad_num)

### PART TWO
print('---PART TWO---')


def contiguous_sum(li: List[int], targ: int) -> List[int]:
    i = 0
    j = 1
    while j < len(li):
        tot = sum(li[i:j])
        if tot == targ:
            return li[i:j]
        elif tot < targ:
            # expand range to right
            j += 1
        else:
            # shorten range from left
            i += 1

        # just double checking
        if i > j:
            raise Exception('hmm.')


contig = contiguous_sum(inp, bad_num)
print(min(contig) + max(contig))

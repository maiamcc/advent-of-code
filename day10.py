#! /usr/bin/env python

from collections import defaultdict
from typing import Dict, List, Set

from utils import read_file


### PART ONE
print('---PART ONE---')
inp = read_file('input/input10', typ=int)

sample = [int(x) for x in """16
10
15
5
1
11
7
19
6
12
4""".split()]


def all_adaptors_including_start_and_builtin(starting_adaptors: List[int]) -> List[int]:
    # given starting adaptor list, add your device's built-in joltage adaptor
    # (3 greater than highest-rated adaptor)
    highest = max(starting_adaptors)
    all_adaptors = [0] + [ad for ad in starting_adaptors] + [highest+3]
    return sorted(all_adaptors)


def find_diffs(ordered_adaptors: List[int]) -> Dict[int, int]:
    diffs = defaultdict(int)
    for i, ad in enumerate(ordered_adaptors):
        if i == 0:
            continue
        diff = ordered_adaptors[i] - ordered_adaptors[i-1]
        if diff > 3:
            raise Exception('wait fuck')
        diffs[diff] += 1

    return diffs


# "how to connect all the adaptors" = sort min -> max
all_adaptors = all_adaptors_including_start_and_builtin(inp)

diffs = find_diffs(all_adaptors)
print(diffs[1] * diffs[3])

### PART TWO
print('---PART TWO---')

all_sample = all_adaptors_including_start_and_builtin(sample)
def count_adaptor_configs(adaptors: List[int], start_i: int=0) -> int:
    #
    # possible_next = valid_next_indexes(adaptors, start_i)
    #
    # if not possible_next:
    #     # womp womp, this configuration doesn't work, backtrack
    #     return None
    #
    # for possible in possible_next:
    #     adaptors_cp = adaptors.copy()
    #     adaptors_cp.remove(possible)
    #     so_far_cp = so_far.copy()
    #     so_far_cp.append(possible)
    #
    #     attempt = find_adaptor_order(adaptors_cp, possible, so_far=so_far_cp)
    #
    #     if attempt:
    #         return attempt
    count = 1
    for i in range(1, len(adaptors)-1):
        dispensible = (adaptors[i+1] - adaptors[i-1] <= 3)
        if dispensible:
            count *= 2
    return count


def valid_next_indexes(adaptors: List[int], i: int) -> List[int]:
    """Which indexes contain an adaptor that can legally plug into the adaptor at index i?"""
    res = []
    for j in range(i+1, i+4):
        if adaptors[j] <= adaptors[i] + 3:
            res.append(j)
        else:
            break

    return res

sample2 = [int(x) for x in """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split()]
all_sample_2 = all_adaptors_including_start_and_builtin(sample2)
print(count_adaptor_configs(all_sample_2))
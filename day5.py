#! /usr/bin/env python
from utils import read_file

from collections import defaultdict
from math import ceil, floor

MAX_ROWS = 127
MAX_COLS = 7

### PART ONE
print('---PART ONE---')
inp = read_file('input/input5')


def get_row(s: str) -> int:
    start = 0
    end = MAX_ROWS
    # print('\t{} --> {}'.format(start, end))
    for ch in s:
        # print(ch)
        if ch == 'F':
            end = start + floor((end - start) / 2)
        elif ch == 'B':
            start = start + ceil((end - start) / 2)
        # print('\t{} --> {}'.format(start, end))

    return start


def get_col(s: str) -> int:
    start = 0
    end = MAX_COLS
    # print('\t{} --> {}'.format(start, end))
    for ch in s:
        # print(ch)
        if ch == 'L':
            end = start + floor((end - start) / 2)
        elif ch == 'R':
            start = start + ceil((end - start) / 2)
        # print('\t{} --> {}'.format(start, end))

    return start


def parse_seat(s: str) -> (int, int):
    return get_row(s[:7]), get_col(s[7:])


def seat_id(row: int, col: int) -> int:
    return row * 8 + col


print(max([seat_id(*parse_seat(seat)) for seat in inp]))

### PART TWO
print('---PART TWO---')
all_seats = defaultdict(dict)
for seat in inp:
    row, col = parse_seat(seat)
    all_seats[row][col] = seat_id(row, col)

missing_seats = []
for row in range(MAX_ROWS+1):
    for col in range(MAX_COLS+1):
        if not all_seats[row].get(col):
            missing_seats.append(seat_id(row, col))


# Could do this by just examining the list but for completionism's sake, will do it programmatically
missing_non_contiguous = []
prev = -1
for i, id in enumerate(missing_seats):
    if i != 0 and missing_seats[i-1] != id-1 and i != len(missing_seats) - 1 and missing_seats[i+1] != id + 1:
        missing_non_contiguous.append(id)
    prev = id

print(missing_non_contiguous)

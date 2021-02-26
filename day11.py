#! /usr/bin/env python

from collections import defaultdict, namedtuple
from typing import List

from utils import read_file

Coord = namedtuple('Coord', ['x', 'y'])

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

### PART ONE
print('---PART ONE---')
inp = read_file('input/input11')

class Map():
    def __init__(self, inp: List[str]):
        self.cur = [[ch for ch in row] for row in inp]
        self.prev = None
        self.next = None
        self.width = len(inp[0])
        self.height = len(inp)

    def print_cur(self):
        for row in self.cur:
            print(' '.join(row))

    def _all_coords(self) -> List[Coord]:
        res = []
        for x in range(self.width):
            for y in range(self.height):
                res.append(Coord(x, y))
        return res

    def _empty_grid(self) -> List[List[str]]:
        return [['_'] * self.width for _ in range(self.height)]

    def _valid(self, coord: Coord) -> bool:
        return not(coord.x < 0 or coord.x >= self.width or coord.y < 0 or coord.y >= self.height)

    def _adjacent_coords(self, coord: Coord) -> List[Coord]:
        if not self._valid(coord):  # there's probs a way to do this as a decorator?
            raise Exception('invalid coordinate: {}'.format(coord))
        res = []
        for x in range(coord.x - 1, coord.x + 2):
            if 0 <= x < self.width:
                for y in range(coord.y - 1, coord.y + 2):
                    if 0 <= y < self.height:
                        # you're not adjacent to yourself
                        if not (x == coord.x and y == coord.y):
                            res.append(Coord(x, y))
        return res

    def _get(self, coord: Coord) -> str:
        if not self._valid(coord):  # there's probs a way to do this as a decorator?
            raise Exception('invalid coordinate: {}'.format(coord))

        return self.cur[coord.y][coord.x]

    @staticmethod
    def _set_grid_at(grid: List[str], coord: Coord, val: str):
        grid[coord.y][coord.x] = val

    # I don't really care about all the values, just how many times each shows up
    def _val_counts_for_coords(self, coords: List[Coord]):
        res = defaultdict(int)
        for c in coords:
            res[self._get(c)] += 1

        return res

    def _adjacent_val_counts(self, coord: Coord):
        if not self._valid(coord):  # there's probs a way to do this as a decorator?
            raise Exception('invalid coordinate: {}'.format(coord))

        return self._val_counts_for_coords(self._adjacent_coords(coord))

    def _next_state(self, coord) -> str:
        if not self._valid(coord):  # there's probs a way to do this as a decorator?
            raise Exception('invalid coordinate: {}'.format(coord))

        val = self._get(coord)
        if val == FLOOR:
            return FLOOR

        adjacents = self._adjacent_val_counts(coord)
        # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        if val == EMPTY and not adjacents[OCCUPIED]:
            return OCCUPIED
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        elif val == OCCUPIED and adjacents[OCCUPIED] >= 4:
            return EMPTY

        # Otherwise, the seat's state does not change.
        return val

    def transform(self):
        # there's probably a clever way to do this in place but for now I'll just put everything
        # into a new grid so I don't need to worry about accidentally basing state transitions off of future state
        nxt = self._empty_grid()
        for c in self._all_coords():
            nxt_state = self._next_state(c)
            self._set_grid_at(nxt, c, nxt_state)

        self.prev = self.cur
        self.cur = nxt

    def transform_loop(self):
        while self.prev != self.cur:
            print('.', end='', flush=True)
            self.transform()

    def count_occupied(self):
        counts = self._val_counts_for_coords(self._all_coords())
        return counts[OCCUPIED]



test = [
    '#.##.##.##',
    '#######.##',
    '#.#.#..#..',
    '####.##.##',
    '#.##.##.##',
    '#.#####.##',
    '..#.#.....',
    '##########',
    '#.######.#',
    '#.#####.##',
]
m = Map(inp)
print('{} x {}'.format(m.width, m.height))
print('---')
m.transform_loop()
# m.print_cur()
print('occupied:', m.count_occupied())



### PART TWO
# print('---PART TWO---')

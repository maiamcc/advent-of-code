#! /usr/bin/env python
from typing import List

from utils import read_file

### PART ONE
inp = read_file('input/input3')

def count_trees(landscape: List[str], slope_x: int, slope_y: int) -> int:
	x = 0
	y = 0
	width = len(landscape[0])
	tree_count = 0
	while y < len(landscape):
		if landscape[y][x] == "#":
			tree_count += 1
		x = (x + slope_x) % width
		y = y + slope_y
	return tree_count

print('---PART ONE---')
print(count_trees(inp, 3, 1))

### PART TWO
print('---PART TWO---')

# haha, I've already parameterized the slope so I don't even need to
# change my function! Go me!
m1 = count_trees(inp, 1, 1)
m2 = count_trees(inp, 3, 1)
m3 = count_trees(inp, 5, 1)
m4 = count_trees(inp, 7, 1)
m5 = count_trees(inp, 1, 2)
print(m1 * m2 * m3 * m4 * m5)

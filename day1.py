#! /usr/bin/env python
from collections import defaultdict

from utils import read_file

# PART ONE
def find_prod(li):
	seen = set()
	for elem in li:
		if 2020-elem in seen:
			return elem * (2020-elem)
		seen.add(elem)

inp = read_file('input/input1', typ=int)

print('PART ONE:', find_prod(inp))

### PART TWO
def twosum(li, targ, elem_counts=None):
	if elem_counts is None:
		elem_counts = defaultdict(int)
		for elem in li:
			elem_counts[elem] += 1

	for elem in li:
		if targ-elem in elem_counts and (elem != targ-elem or elem_counts[elem] >= 2):
			return elem, targ-elem

	return None

def threesum(li, targ=2020, elem_counts=None):
	if elem_counts is None:
		elem_counts = defaultdict(int)
		for elem in li:
			elem_counts[elem] += 1

	for elem in li:
		twosum_elems = twosum(li, targ-elem, elem_counts)
		if twosum_elems and elem not in twosum_elems:
			return (elem, twosum_elems[0], twosum_elems[1])

threesum_elems = threesum(inp, 2020)
print('PART TWO:', threesum_elems[0]*threesum_elems[1]*threesum_elems[2])

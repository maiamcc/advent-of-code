#! /usr/bin/env python
import re

from utils import read_file

regex = re.compile('(\d+)-(\d+) (\w): ([a-z]*)')

# PART ONE
def parse_input_row(row):
	m = regex.match(row)
	if not m:
		raise ValueError('Not enough regex matches for:', row)
	grps = m.groups()
	if len(grps) != 4:
		raise ValueError('Not enough regex matches for:', row)
	return int(grps[0]), int(grps[1]), grps[2], grps[3]

def meets_policy1(min_count, max_count, letter, pword, ):
	count = 0
	for ch in pword:
		if ch == letter:
			count += 1
	return min_count <= count <= max_count

def count_valid(inp, checker):
	valid = 0
	for row in inp:
		if checker(*parse_input_row(row)):
			valid += 1
	return valid

inp = read_file('input/input2')

print('PART ONE:')
# print(meets_policy1(1, 3, 'a', 'abcde'))
# print(meets_policy1(1, 3, 'b', 'cdefg'))
# print(meets_policy1(2, 9, 'c', 'ccccccccc'))
# print(parse_input_row('1-3 a: abcde'))
print(count_valid(inp, meets_policy1))

### PART TWO
def meets_policy2(pos1, pos2, letter, pword):
	i = pos1 - 1  # adjust for 0-index
	j = pos2 - 1  # adjust for 0-index
	in_pos_1 = pword[i] == letter
	in_pos_2 = pword[j] == letter
	return in_pos_1 + in_pos_2 == 1

print('PART TWO:')
# print(meets_policy2(1, 3, 'a', 'abcde'))
# print(meets_policy2(1, 3, 'b', 'cdefg'))
# print(meets_policy2(2, 9, 'c', 'ccccccccc'))
print(count_valid(inp, meets_policy2))

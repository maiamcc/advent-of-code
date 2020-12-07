#! /usr/bin/env python
from functools import partial
import re

from utils import read_file

### PART ONE
print('---PART ONE---')

def parse_passport_str(s):
	s = s.replace('\n', ' ')
	info = {item.split(':')[0]: item.split(':')[1] for item in s.split(' ')}
	return info

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def is_valid1(passport):
	for field in REQUIRED_FIELDS:
		if field not in passport.keys():
			return False
	return True

def count_valid(passports, checker):
	return sum([1 for passport in passports if checker(passport)])

inp = read_file('input/input4', sep='\n\n')
infos = [parse_passport_str(s) for s in inp]
print(count_valid(infos, is_valid1))

### PART TWO
print('---PART TWO---')
def is_valid2(passport):
	for field in REQUIRED_FIELDS:
		val = passport.get(field)
		if not val:
			return False
		if not VALIDATORS[field](val):
			return False
	return True

def between_inclusive(num, x, y):
	if isinstance(num, str):
		if not num.isnumeric():
			return False
		num = int(num)
	return x <= num <= y

COLOR_RE = re.compile('^#[0-9a-z]{6}$')
def hair_color(s):
	return bool(COLOR_RE.match(s))

def height(s):
	if s.endswith('cm'):
		value = s[:len(s)-2]
		return between_inclusive(value, 150, 193)
	elif s.endswith('in'):
		value = s[:len(s)-2]
		return between_inclusive(value, 59, 76)
	return False

EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
def eye_color(s):
	return s in EYE_COLORS

def passport_id(s):
	return s.isnumeric and len(s) == 9

VALIDATORS = {
	'byr': partial(between_inclusive, x=1920, y=2002),
	'iyr': partial(between_inclusive, x=2010, y=2020),
	'eyr': partial(between_inclusive, x=2020, y=2030),
	'hgt': height,
	'hcl': hair_color,
	'ecl': eye_color,
	'pid': passport_id,
}

print(count_valid(infos, is_valid2))

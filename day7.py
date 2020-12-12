#! /usr/bin/env python
from collections import defaultdict, namedtuple
import re
from typing import Dict, List

from utils import read_file

ContentsRule = namedtuple('ContentsRule', ['num', 'color'])


### PART ONE
print('---PART ONE---')
inp = read_file('input/input7')


row_regex = re.compile(r'([a-z]+ [a-z]+) bags contain (.*)\.')
rule_regex = re.compile(r'(\d+) ([a-z]+ [a-z]+) bag')


# PART ONE
class Rules():
    def __init__(self, contains: Dict[str, List[ContentsRule]] = None, is_container_by: Dict[str, List[str]] = None):
        if contains is None:
            contains = {}
        if is_container_by is None:
            is_container_by = defaultdict(list)
        self.contains = contains
        self.is_contained_by = is_container_by

    def add_rule(self, containing_color: str, contents_rules: List[ContentsRule]):
        self.contains[containing_color] = contents_rules
        for cr in contents_rules:
            self.is_contained_by[cr.color].append(containing_color)

    def find_all_containers(self, color: str):
        containers = self.is_contained_by[color]
        res = []
        for c in containers:
            res.extend(self.find_all_containers(c))
        return list(set(containers+res))

    def find_all_bags_inside(self, color: str):
        count = 0
        bags_inside = self.contains[color]
        if not bags_inside:
            return 0
        for bi in bags_inside:
            inside = self.find_all_bags_inside(bi.color)
            extra = bi.num * (inside + 1)  # all the bags inside that bag, plus the bag itself
            count += extra

        return count


def parse_input_row(row: str) -> (str, List[ContentsRule]):
    m = row_regex.match(row)
    if not m:
        raise ValueError('Not enough regex matches for:', row)
    grps = m.groups()
    if len(grps) != 2:
        raise ValueError('Not enough regex matches for:', row)
    color = grps[0]
    return color, parse_contents_rule(grps[1])


def parse_contents_rule(rules_str: str) -> List[ContentsRule]:
    if rules_str == 'no other bags':
        return []
    return [parse_contents_rules(rule_str) for rule_str in rules_str.split(', ')]


def parse_contents_rules(rule_str: str) -> ContentsRule:
    # 5 light blue bags --> ContentsRule(color='light blue', num=5)
    m = rule_regex.match(rule_str)
    if not m:
        raise ValueError('Not enough regex matches for:', rule_str)
    grps = m.groups()
    if len(grps) != 2:
        raise ValueError('Not enough regex matches for:', rule_str)
    return ContentsRule(int(grps[0]), grps[1])


def collect_rules(all_rules: List[str]) -> (Dict[str, List[ContentsRule]], Dict[str, List[str]]):
    rules = Rules()
    for row in all_rules:
        containing_color, contents_rules = parse_input_row(row)
        rules.add_rule(containing_color, contents_rules)
    return rules


r = collect_rules(inp)
print(len(r.find_all_containers("shiny gold")))

### PART TWO
print('---PART TWO---')
print(r.find_all_bags_inside("shiny gold"))

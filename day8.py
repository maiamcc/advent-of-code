#! /usr/bin/env python

from typing import List

from utils import read_file


### PART ONE
print('---PART ONE---')
inp = read_file('input/input8')


def exec_until_loop(program: List[str], try_to_fix=False) -> (int, bool):
    # returns: acc value, was_success
    # try_to_fix --> swap one jmp/nop command with the other verb and see if the program completes
    #   may be false because
    #      A. not trying to change the program, just want to see where it loops, or
    #      B. have already made one change to the program and are checking it, don't make any more changes.

    accumulator = 0
    indexes_visited = {0}
    i = 0

    # import pdb; pdb.set_trace()
    while i < len(program):
        verb, arg = parse_line(program[i])
        if verb == 'acc':
            accumulator += arg
            i += 1  # next line
        elif verb == 'jmp':
            if try_to_fix:
                # try changing this to a nop and running again
                copy = [ln for ln in program]
                copy[i] = copy[i].replace('jmp', 'nop')
                acc, was_success = exec_until_loop(copy, try_to_fix=False)
                if was_success:
                    return acc, was_success
            i += arg
        elif verb == 'nop':
            if try_to_fix:
                # try changing this to a jmp and running again
                copy = [ln for ln in program]
                copy[i] = copy[i].replace('nop', 'jmp')
                acc, was_success = exec_until_loop(copy, try_to_fix=False)
                if was_success:
                    return acc, was_success
            i += 1
        else:
            raise KeyError('Unrecognized verb {}'.format(verb))

        if i in indexes_visited:
            # found a loop! (was_success = false)
            return accumulator, False
        else:
            indexes_visited.add(i)

    # successful termination!
    return accumulator, True


def parse_line(line: str) -> (str, int):
    parts = line.split()
    return parts[0], int(parts[1])


### PART ONE
print(exec_until_loop(inp))


### PART TWO
print('---PART TWO---')
print(exec_until_loop(inp, try_to_fix=True))

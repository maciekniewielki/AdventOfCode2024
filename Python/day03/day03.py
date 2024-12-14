from Common import *
import re


ENABLED = 1
regex_mult = r"mul\(\d{1,3},\d{1,3}\)"
regex_do = r"do\(\)"
regex_dont = r"don't\(\)"


def mul(a, b):
    return a * b * ENABLED


def do():
    global ENABLED
    ENABLED = 1
    return 0


def don_t():
    global ENABLED
    ENABLED = 0
    return 0


def find_instructions(data, only_mult=True):
    if only_mult:
        regex = regex_mult
    else:
        regex = f"{regex_mult}|{regex_do}|{regex_dont}"

    # Convert don't to don_t
    return map(lambda x: x.replace("'", "_"), re.findall(regex, data))


def solve1(data):
    # Please don't run this in production code
    return sum(eval(mult) for mult in find_instructions(data))


def solve2(data):
    return sum(eval(mult) for mult in find_instructions(data, only_mult=False))


# IO
a = input_as_string("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))

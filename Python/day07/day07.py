from Common import *
import re
from itertools import product


def calculate(nums, operators):
    accumulator = nums[0]
    for num, op in zip(nums[1:], operators):
        if op == "+":
            accumulator += num
        elif op == "*":
            accumulator *= num
        elif op == "||":
            accumulator = int(f"{accumulator}{num}")
    return accumulator


def can_be_true(result, nums, possible_ops):
    operation_combinations = product(possible_ops, repeat=len(nums) - 1)
    return any(
        calculate(nums, operators) == result for operators in operation_combinations
    )


def solve1(cases):
    return sum(
        result for result, nums in cases if can_be_true(result, nums, ["+", "*"])
    )


# This can take ~20s to run
def solve2(cases):
    return sum(
        result for result, nums in cases if can_be_true(result, nums, ["+", "*", "||"])
    )


# IO
a = input_as_lines("input.txt")
cases = []
for line in a:
    result, *nums = [int(x) for x in re.findall("\d+", line)]
    cases.append((result, nums))


# 1st
print(solve1(cases))


# 2nd
print(solve2(cases))

from Common import *
from collections import defaultdict


def run_sim(stones):
    new_stones = defaultdict(int)
    for stone in stones:
        new_values = apply_rules(stone)
        for new_value in new_values:
            new_stones[new_value] += stones[stone]
    return new_stones


def apply_rules(stone):
    if stone == 0:
        return [1]

    s = str(stone)
    length = len(s)
    if length % 2 == 0:
        length_halved = length // 2
        return [int(s[:length_halved], 10), int(s[length_halved:], 10)]

    return [stone * 2024]


def solve1(stones):
    for _ in range(25):
        stones = run_sim(stones)

    return sum(stones.values())


def solve2(stones):
    for _ in range(75):
        stones = run_sim(stones)

    return sum(stones.values())


# IO
a = input_as_one_line_ints("input.txt", " ")
stones = defaultdict(int)
for num in a:
    stones[num] += 1

# 1st
print(solve1(stones))

# 2nd
print(solve2(stones))

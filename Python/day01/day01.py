from Common import *


def solve1(data):
    sorted_cols = [list(sorted(c)) for c in data]
    return sum(abs(x - y) for x, y in zip(*sorted_cols))


def solve2(data):
    score = lambda x: x * len([y for y in data[1] if y == x])
    return sum(score(x) for x in data[0])


# IO
a = input_as_column_ints("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))

from Common import *

X_MAS_PATTERNS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],       # Horizontal
    [(0, 0), (0, 1), (0, 2), (0, 3)],       # Vertical
    [(0, 0), (1, 1), (2, 2), (3, 3)],       # Diagonal down
    [(0, 0), (1, -1), (2, -2), (3, -3)],    # Diagonal up
]
REVERSE_X_MAS_PATTERNS = [list(match[::-1]) for match in X_MAS_PATTERNS]
ALL_X_MAS_PATTERNS = X_MAS_PATTERNS + REVERSE_X_MAS_PATTERNS


MAS_PATTERNS = [
    [(0, 0), (1, 1), (2, 2), (2, 0), (1, 1), (0, 2)],  # From left
    [(0, 0), (1, 1), (2, 2), (0, 2), (1, 1), (2, 0)],  # From up
]
REVERSE_MAS_PATTERNS = [list(match[::-1]) for match in MAS_PATTERNS]
ALL_MAS_PATTERNS = MAS_PATTERNS + REVERSE_MAS_PATTERNS


class non_wrap_list(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError()
        return list.__getitem__(self, n)


def count_matches(data, patterns):
    s = 0
    for j in range(len(data)):
        for i in range(len(data[j])):
            s += count_matches_from(data, i, j, patterns)
    return s


def count_matches_from(data, i, j, patterns):
    return sum(is_match_for_pattern(data, i, j, pattern) for pattern in patterns)


def is_match_for_pattern(data, i, j, pattern):
    if len(pattern) == 4:
        word_to_match = "XMAS"
    else:
        word_to_match = "MASMAS"

    try:
        word = "".join([data[j + x][i + y] for x, y in pattern])
        return word == word_to_match
    except IndexError:
        return False


def solve1(data):
    return count_matches(data, ALL_X_MAS_PATTERNS)


def solve2(data):
    return count_matches(data, ALL_MAS_PATTERNS)


# IO
a = input_as_2d_grid("input.txt")
a = non_wrap_list(non_wrap_list(line) for line in a)

# 1st
print(solve1(a))


# 2nd
print(solve2(a))

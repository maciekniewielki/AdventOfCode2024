from Common import *
from itertools import combinations
from collections import defaultdict


def is_inside(pos, size):
    return (0 <= pos[0] < size[0]) and (0 <= pos[1] < size[1])


def add_vects(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def neg_vect(pos):
    return -pos[0], -pos[1]


def sub_vects(pos1, pos2):
    return add_vects(pos1, neg_vect(pos2))


def get_antinodes_of_type(antennas_of_type, size, part2=False):
    return {
        antenna
        for pos1, pos2 in combinations(antennas_of_type, 2)
        for antenna in get_antinodes(pos1, pos2, size, part2)
    }


def get_antinodes(pos1, pos2, size, part2):
    vect_1_2 = sub_vects(pos2, pos1)
    if not part2:
        all_antinodes = {add_vects(pos2, vect_1_2), sub_vects(pos1, vect_1_2)}
        return {pos for pos in all_antinodes if is_inside(pos, size)}

    current_pos1 = pos1
    all_antinodes = set()
    while is_inside(current_pos1, size):
        all_antinodes.add(current_pos1)
        current_pos1 = sub_vects(current_pos1, vect_1_2)

    current_pos2 = pos2
    while is_inside(current_pos2, size):
        all_antinodes.add(current_pos2)
        current_pos2 = add_vects(current_pos2, vect_1_2)

    return all_antinodes


def solve1(antennas, size):
    antinodes = set()
    for type in antennas:
        antinodes |= get_antinodes_of_type(antennas[type], size)
    return len(antinodes)


def solve2(antennas, size):
    antinodes = set()
    for type in antennas:
        antinodes |= get_antinodes_of_type(antennas[type], size, True)
    return len(antinodes)


# IO
a = input_as_2d_grid("input.txt")
antennas = defaultdict(list)
for j, line in enumerate(a):
    for i, char in enumerate(line):
        if char == ".":
            continue
        antennas[char].append((i, j))

size = len(a[0]), len(a)


# 1st
print(solve1(antennas, size))


# 2nd
print(solve2(antennas, size))

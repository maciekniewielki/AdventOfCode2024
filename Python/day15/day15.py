from Common import *
from collections import namedtuple

Vector = namedtuple("Vector", ["x", "y"])

LETTER_TO_DIRECTION = {
    "^": Vector(0, -1),
    "v": Vector(0, 1),
    "<": Vector(-1, 0),
    ">": Vector(1, 0),
}


def print_map(map):
    print("\n".join("".join(line) for line in map))
    print("\n")


def find_object(map, obj):
    for j, line in enumerate(map):
        for i, char in enumerate(line):
            if char == obj:
                yield Vector(i, j)


def add(v1, v2):
    return Vector(v1.x + v2.x, v1.y + v2.y)


def gps(pos):
    return pos.y * 100 + pos.x


def move(pos, vector, map):
    dest = add(pos, vector)
    dest_object = map[dest.y][dest.x]
    if dest_object == "#":
        return False
    elif dest_object == ".":
        map[dest.y][dest.x], map[pos.y][pos.x] = map[pos.y][pos.x], "."
        return True
    else:
        moved = move(dest, vector, map)
        if moved:
            map[dest.y][dest.x], map[pos.y][pos.x] = map[pos.y][pos.x], "."
            return True
    return False


def solve1(map, instructions):
    robot_pos = next(find_object(map, "@"))
    for instruction in instructions:
        vect = LETTER_TO_DIRECTION[instruction]
        moved = move(robot_pos, vect, map)
        if moved:
            robot_pos = add(robot_pos, vect)
    return sum(gps(pos) for pos in find_object(map, "O"))


def solve2(map, instructions):
    pass


# IO
a = input_as_chunks("input.txt")
map_lines, instruction_lines = a
instructions = "".join(instruction_lines)
map = [list(line) for line in map_lines]

# 1st
print(solve1(map, instructions))

# 2nd
# print(solve2(map, instructions))

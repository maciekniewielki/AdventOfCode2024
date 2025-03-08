from Common import *
from collections import namedtuple

Vector = namedtuple("Vector", ["x", "y"])

LETTER_TO_DIRECTION = {
    "^": Vector(0, -1),
    "v": Vector(0, 1),
    "<": Vector(-1, 0),
    ">": Vector(1, 0),
}


def find_object(map, obj):
    for j, line in enumerate(map):
        for i, char in enumerate(line):
            if char == obj:
                yield Vector(i, j)


def add(v1, v2):
    return Vector(v1.x + v2.x, v1.y + v2.y)


def gps(pos):
    return pos.y * 100 + pos.x


def clone_map(map):
    return [line[:] for line in map]


def run_simulation(map, instructions):
    map = clone_map(map)
    robot_pos = next(find_object(map, "@"))
    for instruction in instructions:
        vect = LETTER_TO_DIRECTION[instruction]
        moved = move(robot_pos, vect, map)
        if moved:
            robot_pos = add(robot_pos, vect)
    return map


def move(pos, vector, map):
    dest = add(pos, vector)
    dest_object = map[dest.y][dest.x]
    # Wall
    if dest_object == "#":
        return False
    # Empty space
    elif dest_object == ".":
        map[dest.y][dest.x], map[pos.y][pos.x] = map[pos.y][pos.x], "."
        return True
    # Single box or horizontal double box
    elif dest_object == "O" or (dest_object in "[]" and vector.y == 0):
        moved = move(dest, vector, map)
        if moved:
            map[dest.y][dest.x], map[pos.y][pos.x] = map[pos.y][pos.x], "."
            return True
    # Vertical double box
    else:
        if dest_object == "[":
            left = dest
            right = Vector(dest.x + 1, dest.y)
        else:
            left = Vector(dest.x - 1, dest.y)
            right = Vector(dest.x, dest.y)

        cloned = clone_map(map)
        # Perform move on a copy of the map to be able to rollback in case they're not moved at the same time
        left_moved, right_moved = move(left, vector, cloned), move(
            right, vector, cloned
        )
        if left_moved and right_moved:
            # Ok, we are good. Move them for real
            move(left, vector, map)
            move(right, vector, map)
            map[dest.y][dest.x], map[pos.y][pos.x] = map[pos.y][pos.x], "."
            return True

    return False


def solve1(map, instructions):
    result = run_simulation(map, instructions)
    return sum(gps(pos) for pos in find_object(result, "O"))


def solve2(map, instructions):
    map_extended = [flatten([extend_character(char) for char in line]) for line in map]
    result = run_simulation(map_extended, instructions)
    return sum(gps(pos) for pos in find_object(result, "["))


# IO
def extend_character(char):
    if char == "@":
        return ["@", "."]
    elif char == "O":
        return ["[", "]"]
    else:
        return [char] * 2


a = input_as_chunks("input.txt")
map_lines, instruction_lines = a
instructions = "".join(instruction_lines)
map = [list(line) for line in map_lines]

# 1st
print(solve1(map, instructions))

# 2nd
print(solve2(map, instructions))

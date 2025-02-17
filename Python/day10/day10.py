from Common import *

NEIGHBORS_DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_possible_neighbors(pos):
    return [
        (pos[0] + direction[0], pos[1] + direction[1])
        for direction in NEIGHBORS_DIRECTIONS
    ]


def is_inside(pos, grid):
    height, width = len(grid), len(grid[0])
    return (0 <= pos[0] < width) and (0 <= pos[1] < height)


def get_trailheads(grid):
    return [
        (i, j)
        for j, line in enumerate(grid)
        for i, character in enumerate(line)
        if character == "0"
    ]


def calc_score(trailhead, grid, part2=False):
    if part2:
        return traverse(trailhead, grid, None)
    else:
        return traverse(trailhead, grid, set())


def traverse(pos, grid, previous_positions):
    if previous_positions is not None:
        previous_positions.add(pos)

    current_num = grid[pos[1]][pos[0]]
    if current_num == "9":
        return 1
    next_num = str(int(current_num) + 1)

    to_traverse = []
    for new_pos in get_possible_neighbors(pos):
        if previous_positions is not None and new_pos in previous_positions:
            continue
        if not is_inside(new_pos, grid):
            continue
        if grid[new_pos[1]][new_pos[0]] != next_num:
            continue
        to_traverse.append(new_pos)

    return sum(traverse(p, grid, previous_positions) for p in to_traverse)


def solve1(grid):
    trailheads = get_trailheads(grid)
    return sum(calc_score(trailhead, grid) for trailhead in trailheads)


def solve2(grid):
    trailheads = get_trailheads(grid)
    return sum(calc_score(trailhead, grid, True) for trailhead in trailheads)


# IO
a = input_as_2d_grid("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))

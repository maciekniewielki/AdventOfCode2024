from Common import *
from itertools import product

NEIGHBORS_DIRECTIONS = {(0, 1), (1, 0), (0, -1), (-1, 0)}


def get_all_neighbors(pos):
    return {
        (pos[0] + direction[0], pos[1] + direction[1])
        for direction in NEIGHBORS_DIRECTIONS
    }


def get_all_neighbors_in_grid(pos, grid):
    all_neighbors = get_all_neighbors(pos)

    return {p for p in all_neighbors if is_inside(p, grid)}


def get_all_valid_neighbors(pos, grid):
    neighbors_in_grid = get_all_neighbors_in_grid(pos, grid)
    letter = grid[pos[1]][pos[0]]

    return {p for p in neighbors_in_grid if grid[p[1]][p[0]] == letter}


def get_all_invalid_neighbors(pos, grid):
    return get_all_neighbors(pos) - get_all_valid_neighbors(pos, grid)


def is_inside(pos, grid):
    height, width = len(grid), len(grid[0])
    return (0 <= pos[0] < width) and (0 <= pos[1] < height)


def flood(pos, grid, visited):
    visited.add(pos)
    neighbors = get_all_valid_neighbors(pos, grid)
    for neighbor in neighbors:
        if neighbor not in visited:
            visited |= flood(neighbor, grid, visited)

    return visited


def calculate_perimeter_reduction(pos, neighbors, grid):
    reduction = 0
    # Only spaces where there is no plot of this type
    empty_spaces = get_all_invalid_neighbors(pos, grid)
    for neighbor in neighbors:
        empty_spaces_of_neighbor = get_all_invalid_neighbors(neighbor, grid)
        for pos1, pos2 in product(empty_spaces, empty_spaces_of_neighbor):
            # If a pair of empty spaces is in the same line, the original position and neighbor are as well
            # And they are also not in the center since empty spaces around them exist
            if in_straight_line(pos1, pos2):
                reduction += 1

    # We are counting each line twice, so we have to account for that here
    return reduction / 2


def in_straight_line(pos1, pos2):
    diff = pos1[0] - pos2[0], pos1[1] - pos2[1]
    return diff in NEIGHBORS_DIRECTIONS


def count_price(region, grid, apply_discount):
    area = len(region)
    # Assuming at first that each plot has to be fenced from all sides
    perimeter = 4 * area
    for pos in region:
        neighbors = get_all_valid_neighbors(pos, grid)
        # Reducing the perimeter for each neighbor of the same type
        perimeter -= len(neighbors)
        if apply_discount:
            # Reduce the perimeter further to account for straight lines
            perimeter -= calculate_perimeter_reduction(pos, neighbors, grid)

    return area * int(perimeter)


def calculate_total_cost(grid, apply_discount=False):
    flooded = set()
    regions = []
    for j, line in enumerate(grid):
        for i, _ in enumerate(line):
            if (i, j) in flooded:
                continue
            visited = flood((i, j), grid, set())
            regions.append(visited)
            flooded |= visited
    return sum(count_price(region, grid, apply_discount) for region in regions)


def solve1(grid):
    return calculate_total_cost(grid)


def solve2(grid):
    return calculate_total_cost(grid, True)


# IO
a = input_as_2d_grid("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))

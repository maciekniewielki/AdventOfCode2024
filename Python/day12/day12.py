from Common import *

NEIGHBORS_DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_all_valid_neighbors(pos, grid):
    all_neighbors = [
        (pos[0] + direction[0], pos[1] + direction[1])
        for direction in NEIGHBORS_DIRECTIONS
    ]
    letter = grid[pos[1]][pos[0]]

    return [
        p for p in all_neighbors if is_inside(p, grid) and grid[p[1]][p[0]] == letter
    ]


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


def count_price(region, grid):
    area = len(region)
    # Assuming at first that each plot has to be fenced from all sides
    perimeter = 4 * area
    for pos in region:
        # Reducing the perimeter for each neighbor of the same type
        perimeter -= len(get_all_valid_neighbors(pos, grid))
    return area * perimeter


def solve1(grid):
    flooded = set()
    regions = []
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            if (i, j) in flooded:
                continue
            visited = flood((i, j), grid, set())
            regions.append(visited)
            flooded |= visited
    return sum(count_price(region, grid) for region in regions)


# Awaiting better times
def solve2(grid):
    pass


# IO
a = input_as_2d_grid("input.txt")

# 1st
print(solve1(a))

# 2nd
# print(solve2(grid))

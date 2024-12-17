from Common import *
from itertools import cycle

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

direction_character = {UP: "^", DOWN: "v", LEFT: "<", RIGHT: ">"}


def print_board(obstacles, current_pos, current_direction, width, height):
    for j in range(height):
        for i in range(width):
            if (i, j) in obstacles:
                to_print = "#"
            elif (i, j) == current_pos:
                to_print = direction_character[current_direction]
            else:
                to_print = "."
            print(to_print, end="")

        print()


def identify_entities(board):
    obstacles = set()
    current_pos = None
    for j in range(len(board)):
        for i in range(len(board[j])):
            entity = board[j][i]
            if entity == "#":
                obstacles.add((i, j))
            elif entity == "^":
                current_pos = (i, j)
    return current_pos, obstacles


def inside(board, current_pos):
    width, height = len(board[0]), len(board)
    return (0 <= current_pos[0] < width) and (0 <= current_pos[1] < height)


def one_step(obstacles, current_pos, current_direction, moves):
    new_pos = (
        current_pos[0] + current_direction[0],
        current_pos[1] + current_direction[1],
    )
    if new_pos in obstacles:
        return current_pos, next(moves)
    return new_pos, current_direction


def solve1(board):
    current_pos, obstacles = identify_entities(board)
    current_direction = UP
    seen = set()
    moves = cycle([UP, RIGHT, DOWN, LEFT])
    while inside(board, current_pos):
        seen.add(current_pos)
        current_pos, current_direction = one_step(
            obstacles, current_pos, current_direction, moves
        )
    return len(seen)


def solve2(updates, lookup):
    pass


# IO
a = input_as_2d_grid("input.txt")

# 1st
print(solve1(a))


# 2nd
# print(solve2(a))

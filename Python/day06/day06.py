from Common import *
from itertools import cycle

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


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


def loops(board, obstacles, starting_pos):
    current_pos = starting_pos
    moves = cycle([UP, RIGHT, DOWN, LEFT])
    current_direction = next(moves)
    guard_states = set()
    while inside(board, current_pos):
        current_state = current_pos + current_direction
        # If guard is a second time with the same position and direction
        # then this has to be a loop
        if current_state in guard_states:
            return True
        guard_states.add(current_state)
        current_pos, current_direction = one_step(
            obstacles, current_pos, current_direction, moves
        )

    return False


def solve1(board):
    current_pos, obstacles = identify_entities(board)
    moves = cycle([UP, RIGHT, DOWN, LEFT])
    current_direction = next(moves)
    seen = set()
    while inside(board, current_pos):
        seen.add(current_pos)
        current_pos, current_direction = one_step(
            obstacles, current_pos, current_direction, moves
        )
    return len(seen)

# This can take a minute or so to run
def solve2(board):
    starting_pos, obstacles = identify_entities(board)
    looping_count = 0
    for j in range(len(board)):
        for i in range(len(board[j])):
            if (i, j) == starting_pos or (i, j) in obstacles:
                continue
            obstacles_with_obstruction = set(obstacles)
            obstacles_with_obstruction.add((i, j))
            if loops(board, obstacles_with_obstruction, starting_pos):
                looping_count += 1
    return looping_count


# IO
a = input_as_2d_grid("input.txt")


# 1st
print(solve1(a))


# 2nd
print(solve2(a))

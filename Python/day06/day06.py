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


def get_reachable_positions(board):
    current_pos, obstacles = identify_entities(board)
    moves = cycle([UP, RIGHT, DOWN, LEFT])
    current_direction = next(moves)
    seen = set()
    while inside(board, current_pos):
        seen.add(current_pos)
        current_pos, current_direction = one_step(
            obstacles, current_pos, current_direction, moves
        )
    return seen


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
    return len(get_reachable_positions(board))


# This can take a couple of seconds to run
def solve2(board):
    starting_pos, obstacles = identify_entities(board)
    reachable_positions = get_reachable_positions(board)
    # We only care about putting obstacles
    # if they are in a place the guard will visit
    return sum(
        loops(board, set(obstacles) | {(i, j)}, starting_pos)
        for i, j in reachable_positions
    )


# IO
a = input_as_2d_grid("input.txt")


# 1st
print(solve1(a))


# 2nd
print(solve2(a))

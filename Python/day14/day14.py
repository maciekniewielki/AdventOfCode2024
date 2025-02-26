from Common import *
from collections import namedtuple
import re

Vector = namedtuple("Vector", ["x", "y"])

WIDTH = 101
HEIGHT = 103
MIDDLE_X_INDEX = (WIDTH - 1) // 2
MIDDLE_Y_INDEX = (HEIGHT - 1) // 2

# Mod that returns a positive number when n is negative
def mod(n, m):
    return (n + m) % m


def simulate_n(robot, n):
    pos, vel = robot
    new_pos = Vector(mod(pos.x + n * vel.x, WIDTH), mod(pos.y + n * vel.y, HEIGHT))
    return new_pos, vel


def count_factor(robots):
    quadrants = [0] * 4
    for robot in robots:
        pos, _ = robot
        if 0 <= pos.x < MIDDLE_X_INDEX:
            if 0 <= pos.y < MIDDLE_Y_INDEX:
                quadrants[0] += 1
            elif MIDDLE_Y_INDEX < pos.y:
                quadrants[1] += 1
        elif MIDDLE_X_INDEX < pos.x:
            if 0 <= pos.y < MIDDLE_Y_INDEX:
                quadrants[2] += 1
            elif MIDDLE_Y_INDEX < pos.y:
                quadrants[3] += 1

    factor = 1
    for robots_count in quadrants:
        factor *= robots_count
    return factor


def detect_line_of_robots(robots):
    positions = {robot[0] for robot in robots}
    robots_in_a_row = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x, y) in positions:
                robots_in_a_row += 1
                # Close enough for an image
                if robots_in_a_row > 15:
                    return True
            else:
                robots_in_a_row = 0
    return False


def solve1(robots):
    robots_n = [simulate_n(robot, 100) for robot in robots]
    return count_factor(robots_n)


def solve2(robots):
    for time in range(1, 100000):
        robots = [simulate_n(robot, 1) for robot in robots]
        if detect_line_of_robots(robots):
            return time


# IO
def find_numbers(line):
    return tuple(int(num) for num in re.findall("-?\d+", line))


a = input_as_lines("input.txt")
robots = []
for line in a:
    data = find_numbers(line)
    pos, vel = Vector(*data[:2]), Vector(*data[2:])
    robots.append((pos, vel))


# 1st
print(solve1(robots))

# 2nd
print(solve2(robots))

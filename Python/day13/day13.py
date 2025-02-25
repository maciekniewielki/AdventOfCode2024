from Common import *
from collections import namedtuple
import re

# (a b)
# (c d)
Matrix = namedtuple("Matrix", ["a", "b", "c", "d"])
Vector = namedtuple("Vector", ["x", "y"])


def tokens_for_machine(machine):
    button_a, button_b, prize = machine
    for button_a_presses in range(101):
        for button_b_presses in range(101):
            destination = tuple(
                button_a_presses * button_a_part + button_b_presses * button_b_part
                for button_a_part, button_b_part in zip(button_a, button_b)
            )
            if destination == prize:
                return button_a_presses * 3 + button_b_presses
    return 0


def tokens_for_machine_with_far_prize(machine):
    button_a, button_b, prize = machine
    matrix = Matrix(button_a[0], button_b[0], button_a[1], button_b[1])
    vector = Vector(prize[0] + 10000000000000, prize[1] + 10000000000000)
    result = solve_eq(matrix, vector)

    if result is None:
        return 0

    return int(result.x * 3 + result.y)


def inverse_matrix(m):
    inverted_base = Matrix(m.d, -m.b, -m.c, m.a)
    determinant = m.a * m.d - m.b * m.c
    return inverted_base, determinant


def solve_eq(m, v):
    inv, determinant = inverse_matrix(m)

    # Linearly dependent, however under our assumptions may be solved
    # Since this is only day 13, I hope it won't happen
    # So let's not worry about that and call it a failure
    if determinant == 0:
        return None

    x = (v.x * inv.a + v.y * inv.b) / determinant
    y = (v.x * inv.c + v.y * inv.d) / determinant
    if x.is_integer() and y.is_integer():
        return Vector(x, y)

    return None


def solve1(machines):
    return sum(tokens_for_machine(machine) for machine in machines)


def solve2(machines):
    return sum(tokens_for_machine_with_far_prize(machine) for machine in machines)


# IO
def find_numbers(line):
    return tuple(int(num) for num in re.findall("\d+", line))


a = input_as_chunks("input.txt")
machines = []
for chunk in a:
    button_a = find_numbers(chunk[0])
    button_b = find_numbers(chunk[1])
    prize = find_numbers(chunk[2])
    machines.append((button_a, button_b, prize))


# 1st
print(solve1(machines))

# 2nd
print(solve2(machines))

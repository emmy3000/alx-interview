#!/usr/bin/python3
"""N-Queens Solution Finder Module

This script finds solutions to the N-Queens problem for a given chessboard size.
"""

import sys

solutions = []
"""List of possible solutions to the N-Queens problem."""

n = 0
"""Size of the chessboard."""

pos = None
"""List of possible positions on the chessboard."""


def get_input():
    """Retrieve and validate the program's argument.

    Returns:
        int: The size of the chessboard.
    Raises:
        SystemExit: If the argument is missing or invalid.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Check if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    return pos0[0] == pos1[0] or pos0[1] == pos1[1] or \
        abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Check if a group exists in the list of solutions.

    Args:
        group (list of tuples): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos == grp_pos:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """Build a solution for the N-Queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of tuples): The group of valid positions.
    """
    global solutions, n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a])
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop()


def get_solutions():
    """Get the solutions for the given chessboard size.
    """
    global pos, n
    pos = [(x // n, x % n) for x in range(n ** 2)]
    a = 0
    group = []
    build_solution(a, group)


if __name__ == "__main__":
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)

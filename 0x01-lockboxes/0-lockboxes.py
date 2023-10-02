#!/usr/bin/python3

"""
This module contains a function to determine if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened starting from the first box.

    :param boxes: List of boxes with keys to other boxes.
    :type boxes: list[list[int]]

    :return: True if all boxes can be opened, False otherwise.
    :rtype: bool
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]

    # Mark the first box as visited
    visited[0] = True

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

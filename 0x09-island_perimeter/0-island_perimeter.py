#!/usr/bin/python3
"""
Script name: 0-island_perimeter

Title: Island Perimeter Calculator

Description:
    This script calculates the perimeter of an island
    described in a grid.

Usage:
    ./0-island_perimeter.py

Author:
    Emeka Emodi<emodiemeka@gmail.com>
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    - grid (List[List[int]]): A list of lists representing the island,
    where:
      - 0 represents water
      - 1 represents land

    Returns:
    - int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Check up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check down
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

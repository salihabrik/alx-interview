#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): 2D array of integers representing the island.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Count top perimeter
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Count bottom perimeter
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Count left perimeter
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Count right perimeter
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

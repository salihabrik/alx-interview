#!/usr/bin/python3
"""
This script demonstrates the implementation of a lockbox problem.
"""


def canUnlockAll(boxes):
    """
    Unlock the given lockboxes.

    Args:
        boxes (list): A list of lockboxes, where each box is
        represented by a boolean value.

    Returns:
        list: A list of unlocked boxes.
    """
    box_count = len(boxes)
    visited = [False] * box_count
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < box_count and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

#!/usr/bin/python3
"""
from collections import deque

A module for working with lockboxes
"""
def canUnlockAll(boxes):
    """
    Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    """
    size = len(boxes)
    opened = [False]*size
    opened[0] = True
    queue = deque([0])

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key < size and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)

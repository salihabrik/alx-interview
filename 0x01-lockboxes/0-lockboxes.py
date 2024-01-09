#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
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

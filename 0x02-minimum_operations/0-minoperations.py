#!/usr/bin/python3
"""
Module for minimum operations problem
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations needed.

    Example:
        n = 9
        minOperations(n) => 6
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n /= divisor
        else:
            divisor += 1
    return operations

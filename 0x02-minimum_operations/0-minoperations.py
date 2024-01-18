#!/usr/bin/python3
"""
Module for minimum operations problem
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2

    while n > 1:
        if n % i == 0:
            operations += i
            n = n / i
        else:
            i += 1

    return operations

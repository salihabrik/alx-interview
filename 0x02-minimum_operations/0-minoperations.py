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

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        if dp[i] == 0:
            dp[i] = dp[i - 1] + 1
            for j in range(i * 2, n + 1, i):
                dp[j] = dp[i] + dp[j // i]

    return dp[n]

if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

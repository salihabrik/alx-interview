#!/usr/bin/python3
"""Solve the prime game problem."""


def is_prime(x: int) -> bool:
    """Return True if x is a prime number, False otherwise."""
    if x == 1:
        return False

    # check if x is divisible by any int
    # from 2 to the square root of x
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


# precalculate the number of primes between 1 and n inclusive
# for each n from 1 to 10000 (which is the maximum defined in the problem)
numOfPrimesByN = {}
numOfPrimesByN[0] = 0
count = 0
for i in range(1, 10001):
    if is_prime(i):
        count += 1
    numOfPrimesByN[i] = count


def isWinner(x: int, nums: list) -> str:
    """Return the winner of the game."""
    Maria = Ben = 0
    # for each round
    for i in range(x):
        if numOfPrimesByN[nums[i]] % 2 != 0:
            # there is an odd number of turns -> Maria, the first player, wins
            Maria += 1
        else:
            # there is an even number of turns -> Ben, the second player, wins
            Ben += 1

    if Maria == Ben:
        return None

    return 'Maria' if Maria > Ben else 'Ben'

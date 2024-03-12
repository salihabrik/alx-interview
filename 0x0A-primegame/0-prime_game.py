#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def remove_multiples(numbers, prime):
        return [num for num in numbers if num % prime != 0]

    def play_round(numbers):
        turn = 0  # 0 for Maria, 1 for Ben
        while numbers:
            primes = get_primes(max(numbers))
            found = False
            for prime in primes:
                if prime in numbers:
                    numbers = remove_multiples(numbers, prime)
                    found = True
                    break
            if not found:
                break
            turn = 1 - turn

        return turn

    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        winner = play_round(nums)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

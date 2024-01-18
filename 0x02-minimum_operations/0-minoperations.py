def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    :param n: Integer, the target number of H characters
    :return: Integer, the fewest number of operations needed
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

# Example test cases
n1 = 4
print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))

n2 = 12
print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))

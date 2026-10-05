#!/usr/bin/python3
"""Module for calculating the minimum number of operations

to achieve n characters using Copy All and Paste.
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result

    in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    ops = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1
    return ops

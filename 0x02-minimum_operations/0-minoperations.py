#!/usr/bin/env python3
"""
Calculate minimum operations for reaching n characters
"""


def minOperations(n):
    """ Calculate minimum operations for reaching n characters
    """

    if n <= 1:
        return 0
    else:
        current_factor = 2
        total_operations = 0

        while current_factor <= n:
            if n % current_factor == 0:
                total_operations += current_factor
                n = n / current_factor
            else:
                current_factor += 1

        return total_operations

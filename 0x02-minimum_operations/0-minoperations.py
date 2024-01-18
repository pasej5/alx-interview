#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Minimum Operations """
    if n <= 1:
        return 0
    else:
        i = 2
        c = 0
        while i <= n:
            if n % i == 0:
                c += i
                n = n / i
            else:
                i += 1
        return c
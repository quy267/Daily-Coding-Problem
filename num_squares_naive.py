"""
This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
"""
from math import inf


def recursive_num_squares_naive(n):
    if n == 0:
        return 0

    min_num_squares = inf

    i = 1
    while n - i * i >= 0:
        min_num_squares = min(min_num_squares, recursive_num_squares_naive(n - i * i) + 1)
        i += 1

    return min_num_squares


def dynamic_num_squares_naive(n):
    if n == 0:
        return 0

    cache = [inf for _ in range(n + 1)]
    cache[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            cache[i] = min(cache[i], cache[i - j * j] + 1)
            j += 1

    return cache[n]


print(dynamic_num_squares_naive(13), end='\n')

from collections import defaultdict

"""
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""


def array_two_elements_naive(arr):
    d = defaultdict(int)
    for num in arr:
        d[num] += 1

    result = []
    for num, count in d.items():
        if count == 1:
            result.append(num)
    return result


print(array_two_elements_naive(arr=[2, 4, 6, 8, 10, 2, 6, 10]))

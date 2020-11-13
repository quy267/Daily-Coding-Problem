"""
This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""


def distinct_subarray(arr):
    d = dict()
    result = 0
    longest_subarray_start_index = 0

    for i, e in enumerate(arr):
        if e in d:
            if d[e] >= longest_subarray_start_index:
                result = max(result, i - longest_subarray_start_index)
                longest_subarray_start_index = d[e] + 1
        d[e] = i
    return max(result, len(arr) - longest_subarray_start_index)


if __name__ == '__main__':
    print(distinct_subarray([5, 1, 3, 5, 2, 3, 4, 1]))

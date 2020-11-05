"""This problem was asked by Google.
This problem was asked by Google.
Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
"""


def is_palindrome(s):
    return s == s[::-1]

def split_into_palindromes_recursive(s):
    if not s:
        return []

    if is_palindrome(s):
        return [s]

    min_cut = None

    for i in range(1, len(s)):
        curr_cut = split_into_palindromes_recursive(s[:i]) + split_into_palindromes_recursive(s[i:])

        if min_cut is None or len(curr_cut) < len(min_cut):
            min_cut = curr_cut
    return min_cut


def split_into_palindromes_dynamic(s):
    A = [[None for _ in range(len(s))] for _ in range(len(s))]

    # Set all substrings of length 1 to be true
    for i in range(len(s)):
        A[i][i] = True

    # Try all substrings of length 2
    for i in range(len(s) - 1):
        A[i][i + 1] = s[i] == s[i + 1]

    i, k = 0, 3
    while k <= len(s):
        while i < (len(s) - k + 1):
            j = i + k - 1
            A[i][j] = A[i + 1][j - 1] and s[i] == s[j]
            i += 1
        k += 1
        i = 0

    P = [None for _ in range(len(s) + 1)]
    P[0] = []
    for i in range(len(P)):
        for j in range(i):
            matrix_i = i - 1

            if A[j][matrix_i]:
                if P[i] is None or (len(P[j]) + 1 < len(P[i])):
                    P[i] = P[j] + [s[j:i]]

    return P[-1]


if __name__ == '__main__':
    print(split_into_palindromes_dynamic('racecarannakayak'))

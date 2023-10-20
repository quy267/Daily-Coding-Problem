"""
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""
import sys

"""
Solution
This problem should strike you as recursive. The string should match the regex if we can match the head of the string with the head of the regex and the rest of the string with the rest of the regex. The special characters . and * make implementing this a bit trickier, however, since the * means we can match 0 or any number of characters in the beginning.

The basic idea then is to do the following. Let's call the string we want to match s and the regex r.

Base case: if r is empty, then return whether s is empty or not.
Otherwise, if the first thing in r is not proceeded by a *, then match the first character of both r and s, and if they match, return match(r[1:], s[1:]). If they don't, then return false.
If the first thing in r is proceeded by a *, then try every suffix substring of s on r[2:] and return true if any suffix substring works.
"""


def matches_first_char(string, regular_expression):
    return (len(string) > 0 and string[0] == regular_expression[0]) or (
                regular_expression[0] == '.' and len(string) > 0)


def matches(string, regular_expression):
    if regular_expression == '':
        return string == ''

    if len(regular_expression) == 1 or regular_expression[1] != '*':
        # The first character in the regex is not proceeded by a *.
        if matches_first_char(string, regular_expression):
            return matches(string[1:], regular_expression[1:])
        else:
            return False
    else:
        # The first character is proceeded by a *.
        # First, try zero length.
        if matches(string, regular_expression[2:]):
            return True
        # If that doesn't match straight away, then try globbing more prefixes
        # until the first character of the string doesn't match anymore.
        i = 0
        while matches_first_char(string[i:], regular_expression):
            if matches(string[i + 1:], regular_expression[2:]):
                return True
            i += 1
        return False


if __name__ == '__main__':
    print(matches("raymond", "ra."), '\n')

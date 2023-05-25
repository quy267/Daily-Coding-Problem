"""
This problem was asked by Walmart Labs.

There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such that there are no gaps between any of them, while keeping overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where 0 represents an empty seat and 1 represents a person. In this case, one solution would be to place the person on the right in the fourth seat. We can consider the cost of a solution to be the sum of the absolute distance each person must move, so that the cost here would be five.

Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.
"""


def move(seats):
    people = [i for i, x in enumerate(seats) if x == 1]
    n = len(people)
    median = people[n // 2]
    cost = 0

    # Move left seats closer to median.
    i = median - 1
    j = n // 2 - 1
    while i >= 0 and j >= 0:
        if seats[i] == 0:
            cost += abs(people[j] - i)
            seats[i], seats[people[j]] = seats[people[j]], seats[i]
            j -= 1
        i -= 1

    # Move right seats closer to median.
    i = median + 1
    j = n // 2 + 1
    while i < len(seats) and j < n:
        if seats[i] == 0:
            cost += abs(people[j] - i)
            seats[i], seats[people[j]] = seats[people[j]], seats[i]
            j += 1
        i += 1

    return seats, cost


if __name__ == '__main__':
    print(move(seats=[0, 1, 1, 0, 1, 0, 0, 0, 1]), "\n")

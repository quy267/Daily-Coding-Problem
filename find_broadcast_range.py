"""
This problem was asked by Spotify.

You are the technical director of WSPT radio, serving listeners nationwide. For simplicity's sake we can consider each listener to live along a horizontal line stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers, each placed at various locations along this line, determine what the minimum broadcast range would have to be in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. In this case the minimum range would be 5, since that would be required for the tower at position 15 to reach the listener at position 20.
"""


def search(listener, towers):
    start = 0
    end = len(towers) - 1

    while start < end:
        mid = start + (end - start) // 2

        if towers[mid] < listener:
            start = mid + 1
        elif towers[mid] > listener:
            end = mid
        else:
            return mid

    return start


def find_broadcast_range(listeners, towers):
    min_range = 0
    towers = [-float('inf')] + sorted(towers) + [float('inf')]

    for listener in listeners:
        idx = search(listener, towers)

        left = listener - towers[idx - 1]
        right = towers[idx] - listener

        min_range = max(min_range, min(left, right))

    return min_range


if __name__ == '__main__':
    print(find_broadcast_range(listeners=[1, 5, 11, 20], towers=[4, 8, 15]))

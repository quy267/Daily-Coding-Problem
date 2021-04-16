"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of
each sock, determine how many pairs of socks with matching colors there are.
"""


# Complete the sockMerchant function below.
def sock_merchant(n, ar):
    colors = list()
    pairs = 0

    for i in range(n):
        if colors.count(ar[i]) == 0:
            colors.append(ar[i])
        else:
            pairs += 1
            colors.remove(ar[i])
    return pairs


if __name__ == '__main__':
    result = sock_merchant(n=7, ar=[1, 2, 1, 2, 1, 3, 2])
    print(result, )

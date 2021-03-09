"""
This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""


class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_nodes(ll):
    start = end = ll

    while start:
        end = start
        total = 0
        skip = False

        while end:
            total += end.data
            if total == 0:
                start = end
                skip = True
                break
            end = end.next

        if not skip:
            print(start.data)

        start = start.next


if __name__ == '__main__':
    first = LinkedList(3)
    second = LinkedList(4)
    third = LinkedList(-7)
    fourth = LinkedList(5)
    fifth = LinkedList(-6)
    sixth = LinkedList(6)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth

    print_nodes(first)

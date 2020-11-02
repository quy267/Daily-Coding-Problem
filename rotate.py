"""
#177
This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
"""


# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def __str__(self):

        # defining a blank res variable
        res = ""

        # initializing ptr to head
        ptr = self.head

        # traversing and adding it to res
        while ptr:
            res += str(ptr.data) + ", "
            ptr = ptr.next

        # removing trailing commas
        res = res.strip(", ")

        # chen checking if
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"


def rotate(head, k):
    fast, slow = head, head

    for _ in range(k):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    new_head = slow.next
    fast.next = head
    slow.next = None

    return new_head


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    linked_list.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    print(linked_list)

    linked_list.head = rotate(linked_list.head, 3)

    print(linked_list)

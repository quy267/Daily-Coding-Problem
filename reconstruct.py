"""
This problem was asked by Google.

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8
"""

COUNT = [10]


class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_2d(root, space):
    # Base case
    if root is None:
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print_2d(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    # Process left child
    print_2d(root.left, space)


def reconstruct(postorder):
    if not postorder:
        return None
    elif len(postorder) == 1:
        return BSTNode(postorder[0])

    root_val = postorder[-1]
    root = BSTNode(root_val)

    for i, val in enumerate(postorder[:-1]):
        if val > root_val:
            left_subtree = reconstruct(postorder[:i])
            right_subtree = reconstruct(postorder[i:-1])
            root.left = left_subtree
            root.right = right_subtree
            return root

    left_subtree = reconstruct(postorder[:-1])
    root.left = left_subtree
    return root


if __name__ == '__main__':
    print_2d(reconstruct([2, 4, 3, 8, 7, 5]), 0)

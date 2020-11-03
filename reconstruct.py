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


class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    print(reconstruct([2, 4, 3, 8, 7, 5]))
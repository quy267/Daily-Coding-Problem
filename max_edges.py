"""
This problem was asked by Adobe.

You are given a tree with an even number of nodes. Consider each connection between a parent and child node to be an "edge". You would like to remove some of these edges, such that the disconnected subtrees that remain each have an even number of nodes.

For example, suppose your input was the following tree:

   1
  / \
 2   3
    / \
   4   5
 / | \
6  7  8
In this case, removing the edge (3, 4) satisfies our requirement.

Write a function that returns the maximum number of edges you can remove while still satisfying this requirement.
"""
from collections import defaultdict


def traverse(graph, curr, result):
    descendants = 0

    for child in graph[curr]:
        num_nodes, result = traverse(graph, child, result)

        result[child] += num_nodes - 1
        descendants += num_nodes

    return descendants + 1, result


def max_edges(graph):
    start = list(graph)[0]
    vertices = defaultdict(int)

    _, descendants = traverse(graph, start, vertices)

    return len([val for val in descendants.values() if val % 2 == 1])


if __name__ == '__main__':
    print(max_edges(graph={
        1: [2, 3],
        2: [],
        3: [4, 5],
        4: [6, 7, 8],
        5: [],
        6: [],
        7: [],
        8: []}
    ), "\n")

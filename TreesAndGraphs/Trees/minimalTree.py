# INFO: Minimal Tree
# Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.

from typing import List, Optional, Self


class Node:
    def __init__(self, content):
        self.content = content
        self.left: Optional[Self] = None
        self.right: Optional[Self] = None


def minimal_tree(arr: List):
    mid = len(arr) // 2
    root_index = arr[mid]
    root_node = Node(arr[root_index])

    root_node.left = Node(arr[root_index - 1])
    root_node.right = Node(arr[root_index + 1])

    attach_left(arr[0:mid], root_node.left)
    attach_right(arr[mid:], root_node.right)


def attach_left(arr: List, node: Node):
    pass


def attach_right(arr: List, node: Node):
    pass


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]

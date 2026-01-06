# INFO: Minimal Tree
# Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.

from typing import List, Optional, Self


class Node:
    def __init__(self, content):
        self.content = content
        self.left: Optional[Self] = None
        self.right: Optional[Self] = None


# INFO: Failed attempt at doing it on my own
# def minimal_tree(arr: List) -> Node:
#     mid = len(arr) // 2
#     root_index = arr[mid]
#     root_node = Node(arr[root_index])
#
#     root_node.left = Node(arr[root_index - 1])
#     root_node.right = Node(arr[root_index + 1])
#
#     attach_left(arr[0:mid], root_node.left)
#     attach_right(arr[mid:], root_node.right)
#     return root_node
#
#
# def attach_left(arr: List, node: Node):
#     # in this case the root is the node that has been given to it
#     if len(arr) == 0:
#         return
#     # should check for cases where the len of the array == 1  & 2 also
#     node.right == arr[-2]
#     node.left == arr[-3]
#     attach_left(arr[0:])
#
#
# def attach_right(arr: List, node: Node):
#     if len(arr) == 0:
#         return


# INFO: using hints
# 1: A minimal binary tree has about the same number of nodes on the left of each node
# as on the right. Let's focus on just the root for now. How would you ensure that about the
# same number of nodes are on th left of the root as on the right?

# 2: You could implement this by finding the "ideal" next element to add and repeatedly
# call insertValue. This will be a bit inefficient, as you would have to repeatedly traverse the tree.
# Try recursion instead. Can you divide this problem into subproblems?

# 3: Imagine we had a createMinimalTree method that returns a minimal tree for a given array(bur for some
# strange reason doesn't operate on the root of the tree). Could you use this to operate on the root of
# the tree? Could you write the base case for the function? Great! Then that's basically the entire function

# INFO: failed
# def minimal_tree(arr: List) -> Node:
#     root_index = len(arr) // 2
#     root_val = arr[root_index]
#     root = Node(root_val)
#     for val in arr:
#         insert_value(val,root)
#     return root
#
# def insert_value(value:int,root:Node):
#     #you could either go left or right I guess
#


# Gayles solution:
def minimal_tree(arr: List) -> Optional[Node]:
    return create_minmal_tree(arr, 0, len(arr) - 1)


def create_minmal_tree(arr: List, start: int, end: int) -> Optional[Node]:
    if end < start:
        return None
    mid_index = (start + end) // 2
    root = Node(arr[mid_index])
    root.left = create_minmal_tree(arr, start, mid_index - 1)
    root.right = create_minmal_tree(arr, mid_index + 1, end)
    return root


def in_order_traversal(node: Optional[Node]) -> None:
    if node:
        if node.left:
            in_order_traversal(node.left)
        print(node.content)
        if node.right:
            in_order_traversal(node.right)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    return_node = minimal_tree(array)
    in_order_traversal(return_node)

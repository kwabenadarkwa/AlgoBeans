# INFO: List of Depths
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, youll have D linked lists).Hints: #107,#123, #135
from typing import List

from TreesAndGraphs.TreeNode import BinaryTreeNode

#     10
#    /  \
#   5    15
#  / \   / \
# 3   7 12  17
"""
total = 2^n - 1
(total + 1) = 2^n
(total + 1) = 2^n
log(total+1) = nlog2
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert_at_head(self, value):
        previous_head = self.head
        self.head = ListNode(value)
        self.head.next = previous_head

    def insert_at_tail(self, value):
        if self.is_empty():
            return 

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = ListNode(value)

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next
        print(None)



def createLinkedListFromBinaryTree(tree: BinaryTreeNode) -> List[SinglyLinkedList]:
    elements = []
    get_list_from_binary_tree(tree,elements)
    list_of_linked_lists = []
    import math

    max_linked_list_count = int(math.log(len(elements) + 1, 2))
    for i in range(max_linked_list_count):
        new_linked_list = SinglyLinkedList()
        for j in range(len(elements)):
            if math.floor(math.log(j + 1, 2)) == i:
                new_linked_list.insert_at_head(elements[j])
        list_of_linked_lists.append(new_linked_list)
    return list_of_linked_lists


def get_list_from_binary_tree(tree: BinaryTreeNode,elements):
    if tree is not None:
        # print(tree.value)
        elements.append(tree.value)

        if tree.left :
            get_list_from_binary_tree(tree.left,elements)

        if tree.right:
            get_list_from_binary_tree(tree.right,elements)


if __name__ == "__main__":
    tree1 = BinaryTreeNode(10)
    tree1.left = BinaryTreeNode(5)
    tree1.right = BinaryTreeNode(15)
    tree1.left.left = BinaryTreeNode(3)
    tree1.left.right = BinaryTreeNode(7)
    tree1.right.left = BinaryTreeNode(12)
    tree1.right.right = BinaryTreeNode(17)
    result1 = createLinkedListFromBinaryTree(tree1)
    assert len(result1) == 3
    assert result1[0].head.value == 10
    assert result1[1].head.value == 3
    assert result1[2].head.value == 17

    result1[0].print()
    result1[1].print()
    result1[2].print()
    
    tree2 = BinaryTreeNode(1)
    result2 = createLinkedListFromBinaryTree(tree2)
    assert len(result2) == 1
    result2[0].print()
    assert result2[0].head.value == 1

    tree3 = BinaryTreeNode(1)
    tree3.left = BinaryTreeNode(2)
    tree3.right = BinaryTreeNode(3)
    result3 = createLinkedListFromBinaryTree(tree3)
    assert len(result3) == 2
    assert result3[0].head.value == 1
    assert result3[1].head.value == 3
    
    tree4 = BinaryTreeNode(5)
    tree4.left = BinaryTreeNode(3)
    tree4.left.left = BinaryTreeNode(1)
    tree4.left.right = BinaryTreeNode(4)
    tree4.right = BinaryTreeNode(8)
    tree4.right.left = BinaryTreeNode(6)
    tree4.right.right = BinaryTreeNode(9)
    result4 = createLinkedListFromBinaryTree(tree4)
    assert len(result4) == 3
    assert result4[0].head.value == 5
    # assert result4[1].head.value == 8
    print("for result 4")
    result4[0].print()
    result4[1].print()
    result4[2].print()
    # assert result4[2].head.value == 9

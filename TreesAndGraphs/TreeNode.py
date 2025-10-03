from typing import Optional, Self


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children: list[Self] = []


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional[Self] = None
        self.right: Optional[Self] = None

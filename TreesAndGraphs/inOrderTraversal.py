from TreeNode import BinaryTreeNode


# INFO: an in order traversal means to visit the left node before the actual node
# and then finally the right node
def in_order_traversal(node: BinaryTreeNode) -> None:
    if node: 
        if node.left:
            in_order_traversal(node.left)
        print(node.value)
        if node.right:
            in_order_traversal(node.right)


#INFO: visits the current node before visiting it's kids
def pre_order_traversal(node: BinaryTreeNode) -> None:
    if node: 
        print(node.value)
        if node.left:
            pre_order_traversal(node.left)
        if node.right:
            pre_order_traversal(node.right)

def post_order_traversal(node: BinaryTreeNode) -> None:
    if node: 
        if node.left:
            post_order_traversal(node.left)
        if node.right:
            post_order_traversal(node.right)
        print(node.value)

if __name__ == "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    # in_order_traversal(root)
    # pre_order_traversal(root)
    post_order_traversal(root)

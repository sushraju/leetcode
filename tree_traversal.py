"""BST construction and traversal"""


# !/usr/bin/env python

class Node:
    """Represents a node in a tree with left and right subtrees"""

    def __init__(self, key):
        """Initialize the node"""
        self.left = None
        self.right = None
        self.val = key


def insert_bst(root, node):
    """Function to build a binary search tree"""
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert_bst(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert_bst(root.left, node)


def print_in_order(root):
    """A function to do inorder tree traversal"""
    if root:
        # First recur on left child
        print_in_order(root.left)

        # then print the data of node
        print(root.val)

        # now recur on right child
        print_in_order(root.right)


def print_post_order(root):
    """A function to do postorder tree traversal"""
    if root:
        # First recur on left child
        print_post_order(root.left)

        # the recur on right child
        print_post_order(root.right)

        # now print the data of node
        print(root.val)


def print_pre_order(root):
    """A function to do preorder tree traversal"""
    if root:
        # First print the data of node
        print(root.val)

        # Then recur on left child
        print_pre_order(root.left)

        # Finally recur on right child
        print_pre_order(root.right)


def main():
    """Driver code"""
    root = Node(5)
    insert_bst(root, Node(3))
    insert_bst(root, Node(7))
    insert_bst(root, Node(2))
    insert_bst(root, Node(4))
    insert_bst(root, Node(1))
    insert_bst(root, Node(6))
    insert_bst(root, Node(8))

    print("Preorder traversal of binary tree is")
    print_pre_order(root)

    print("\nInorder traversal of binary tree is")
    print_in_order(root)

    print("\nPostorder traversal of binary tree is")
    print_post_order(root)


if __name__ == "__main__":
    main()

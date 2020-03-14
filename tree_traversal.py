#!/usr/bin/env python

class Node:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)

def main():
    # Driver code
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.left.left.left = Node(1)
    root.right.left = Node(6)
    root.right.right = Node(8)
    print ("Preorder traversal of binary tree is")
    printPreorder(root)

    print ("\nInorder traversal of binary tree is")
    printInorder(root)

    print ("\nPostorder traversal of binary tree is")
    printPostorder(root)

if __name__ == "__main__":
   main()
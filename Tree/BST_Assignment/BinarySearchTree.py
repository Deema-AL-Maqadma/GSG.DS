from Node import Node

# BinarySearchTree class
class BinarySearchTree:

    # The constructor
    def __init__(self):
        self.root = None

#------------------------------------------------------------------------------------------------
    # insert method
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

# ---> Answers of the Assognment //
#------------------------------------------------------------------------------------------------
# Q : 1 / Implement a findMin and findMax method in the BST class

    # findMin method
    def findMin(self):
        current = self.root
        if not current:
            return None
        while current.left:
            current = current.left
        return current.value

    # findMax method
    def findMax(self):
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current.value

#------------------------------------------------------------------------------------------------
# Q : 2 / Write a function that returns True if the binary tree is balanced, and False otherwise.
    
    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def isBalanced(self):
        return self._isBalanced(self.root)

    def _isBalanced(self, node):
        if node is None:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self._isBalanced(node.left) and self._isBalanced(node.right)


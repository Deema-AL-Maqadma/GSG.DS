from Node import BSTNode

class BST:

    # The constructor
    def __init__(self):
          self.root = None

# ---> Answers of the Assognment //
#------------------------------------------------------------------------------------------------
# Q : 1 / Implement a findMin and findMax method in the BST class

    # findMin method
    def findMin(self):
        node = self.root
        if not node:
            return None
        while node.left:
            node = node.left
        return node.data
    
    # findMax method
    def findMax(self):
        node = self.root
        if not node:
            return None
        while node.right:
            node = node.right
        return node.data

#------------------------------------------------------------------------------------------------
# Q : 2 / Write a function that returns True if the binary tree is balanced, and False otherwise.
    def isBalanced(self, node):
        if node is None:
           return True  # empty tree is balanced
        left_height = self.computeHeight(node.left)
        right_height = self.computeHeight(node.right)

        if (left_height - right_height) > 1:
            return False # if deffirence >1 not balanced

        left_balanced = self.isBalanced(node.left)
        right_balanced = self.isBalanced(node.right)

        return left_balanced and right_balanced


 # ---> Answers of the Exercises //
 #------------------------------------------------------------------------------------------------
 # Exercise 1: Tree Traversal

     # Left - Node - Right
    def inorder(self, node):
        if node:
          self.inorder(node.left)
          print(node.data, end=' ')
          self.inorder(node.right)
 

     # Node - Left - Right
    def preorder(self, node):
        if node:
           print(node.data, end=" ")
           self.preorder(node.left)
           self.preorder(node.right)
    

    # Left - Right - Node
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

#------------------------------------------------------------------------------------------------
# Exercise 2: Validate BST

    def isValidBST(self,root):
        return self._validate(root, float('-inf'), float('inf')) # defualt value

    def _validate(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False
        return (self._validate(node.left, min_val, node.data) and
                self._validate(node.right, node.data, max_val))
    

#------------------------------------------------------------------------------------------------
# Exercise 3: Compute the Height of a Binary Tree
    def computeHeight(self, root):
        if root is None:
           return 0
        left_height = self.computeHeight(root.left)
        right_height = self.computeHeight(root.right)
        return max(left_height, right_height) + 1

#------------------------------------------------------------------------------------------------
    # insert method
    def insert(self, data):
       self.root = self._insert(self.root, data)
 
    def _insert(self, node, data):
       if node is None:
           return BSTNode(data)
       if data < node.data:
           node.left = self._insert(node.left, data)
       else:
            node.right = self._insert(node.right, data)
            return node
#------------------------------------------------------------------------------------------------
    # search method
    def search(self, node, target):
        if node is None:
           return False
        if node.data == target:
           return True
        elif target < node.data:
           return self.search(node.left, target)
        else:
           return self.search(node.right, target)

#------------------------------------------------------------------------------------------------
    # delete method
    def delete(self, node, key):
        if node is None:
           return node
        if key < node.data:
           node.left = self.delete(node.left, key)
        elif key > node.data:
           node.right = self.delete(node.right, key)
        else:
           if node.left is None:
              return node.right
           elif node.right is None:
              return node.left
           temp = self.findMin(node.right)
           node.data = temp.data
           node.right = self.delete(node.right, temp.data)
        return node

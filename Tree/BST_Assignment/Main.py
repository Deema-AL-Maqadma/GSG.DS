# Deema Mohammed AL-Maqadma
# Trees and Binary Trees Assignment
# The Implementation
from BinarySearchTree import BinarySearchTree

class Main:
    def run(self):
        bst = BinarySearchTree()
        values = [20, 10, 30, 5, 15, 25, 35]
        for val in values:
            bst.insert(val)

        print("---> Min value:", bst.findMin())          #  5
        print("--->  Max value:", bst.findMax())          #  35
        print("--->  Tree is balanced?", bst.isBalanced()) #  True

#---------------------------------------------------------------
# Usage
Implementation = Main()
print()
Implementation.run()
print("\n---> Thx ^_^ ...\n")

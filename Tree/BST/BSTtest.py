# Deema Mohammed AL-Maqadma
# Trees and Binary Trees Assignment
# The Implementation

from BST import BST
my_tree = BST()
my_tree.insert(5)
my_tree.insert(3)
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(6)

my_tree.inorder(my_tree.root)
print(my_tree.findMax())
print(my_tree.findMin())
# Deema Mohammed AL-Maqadma
# CircularLinkedList LinkedList Assignment
# The Implementation
from CircularLinkedList import SortedCircularLinkedList

#-----------------------------------------------------------
# Usage
# Create the list
scll = SortedCircularLinkedList()
#-----------------------------------------------------------

# befor inserting any element
print("\nCircular LinkedList befor inserting any element: ")
scll.print_list()
print()
#-----------------------------------------------------------

# Insert elements in order: 7, 3, 9, 1, 4
print("After inserting 7:")
scll.insert(7)
scll.print_list()

print("\nAfter inserting 3:")
scll.insert(3)
scll.print_list()

print("\nAfter inserting 9:")
scll.insert(9)
scll.print_list()

print("\nAfter inserting 1:")
scll.insert(1)
scll.print_list()

print("\nAfter inserting 4:")
scll.insert(4)
scll.print_list()
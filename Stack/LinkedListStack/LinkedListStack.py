from Node import Node

class LinkedStack:
    def __init__(self):
       self.top = None

    def push(self, data):
       new_node = Node(data)
       new_node.next = self.top
       self.top = new_node

    def pop(self):
       if self.top is None:
          return None
       to_return = self.top.data
       self.top = self.top.next
       return to_return
    
    def peek(self):
       return None if self.top is None else self.top.data
    
    def is_empty(self):
       return self.top is None
   
    def clear(self):
       self.top = None

    


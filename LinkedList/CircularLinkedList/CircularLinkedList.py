from Node import Node
# CircularLinkedList LinkedList class
class SortedCircularLinkedList:

    def __init__(self):
        self.head = None
    #--------------------------------------------------------------
    # Method to insert
    def insert(self, data):
        new_node = Node(data)
        
        # Case 1: List is empty
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        
        # Case 2: Insert at the beginning (new node is smallest)
        if new_node.data < current.data:
            # Find the last node to update its next pointer
            last = self.head
            while last.next != self.head:
                last = last.next
            
            new_node.next = self.head
            self.head = new_node
            last.next = self.head
            return
        
        # Case 3: Insert somewhere in the middle or end
        while True:
            # Stop if we've found the insertion point
            if current.next == self.head or new_node.data < current.next.data:
                break
            current = current.next
        
        # Insert the new node
        new_node.next = current.next
        current.next = new_node
    
    #--------------------------------------------------------------
    # Method to print list
    def print_list(self):
        if self.head is None:
            print("[]")
            return
        
        current = self.head
        result = []
        
        # Traverse the circular list once
        while True:
            result.append(f"[{current.data}]")
            current = current.next
            if current == self.head:
                break
        
        print(" -> ".join(result))
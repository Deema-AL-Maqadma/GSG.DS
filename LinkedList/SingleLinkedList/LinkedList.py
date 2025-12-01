from Node import Node
# LinkedList class
class LinkedList:
   # constructor
   def __init__(self):
      self.head = None

   # Adds a new node at the beginning.
   def insert_at_start(self, data):
         new_node = Node(data)
         new_node.next = self.head
         self.head = new_node

    # Insert at End
   def insert_at_end(self, data):
      new_node = Node(data)
      if self.head is None:
         self.head = new_node
         return
      last = self.head
      while last.next:
         last = last.next
      last.next = new_node

    # insert a new node based on a given index (position)
   def insert_at_index(self, index, data):
       new_node = Node(data)
       if index == 0:
          self.insert_at_start(data)
          return
       current = self.head
       count = 0
       while current is not None and count < index - 1:
          current = current.next
          count += 1
       if current is None:
           print("Index out of bounds; inserting at the end.")
           self.insert_at_end(data)
       else:
           new_node.next = current.next
           current.next = new_node

    # toString Method
   def __str__(self):
      result = ""
      temp = self.head
      while temp:
         result += f"[{temp.data}]->"
         temp = temp.next
      result += "None"
      return result
   
   # Compute Length
   def length(self):
      count = 0
      temp = self.head
      while temp:
         count += 1
         temp = temp.next
      return count
   
   # Delete from Start
   def delete_at_start(self):
       if self.head:
           self.head = self.head.next

   # Delete from End
   def delete_at_end(self):
       if self.head is None:
           return
       if self.head.next is None:
           self.head = None
           return
       temp = self.head
       while temp.next.next:
           temp = temp.next
       temp.next = None

    # Delete Between Two Nodes
   def delete_node(self, key):
       temp = self.head
       if temp and temp.data == key:
           self.head = temp.next
           return
       prev = None
       while temp and temp.data != key:
            prev = temp
            temp = temp.next
       if temp is None:
           return
       prev.next = temp.next

    # Search for an Item
   def search(self, key):
      temp = self.head
      while temp:
         if temp.data == key:
            return True
         temp = temp.next
      return False

# -----------------------------------------------------------------------------------------------
# ------------->>> Exercises with Linked List  <<<-----------------------------

   
    # Exercise 1: Find the Middle of a Linked List Use slow and fast pointer approach. Display the middle node's value.
   def find_middle(self):
      slow = self.head
      fast = self.head
      while fast and fast.next:
         slow = slow.next
         fast = fast.next.next
      print(slow.data)

    # Another way Using Length
   def find_middle_using_length(self):
    # حساب الطول
    length = 0
    temp = self.head
    while temp:
        length += 1
        temp = temp.next
    # الوصول للعنصر في المنتصف (الثاني إذا العدد زوجي)
    mid = length // 2
    temp = self.head
    for _ in range(mid):
        temp = temp.next
    print(temp.data)

    # Exercise 2: Merge Two Sorted Linked Lists Given two linked lists, write a function to merge them into a new sorted linked list.
   def merge_lists(self,l1, l2):
    merge = LinkedList()
    curr = Node(0)
    while l1 and l2:
        if l1.data < l2.data:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2
    return merge.next
   # Exercise 3: Remove Duplicates Given a linked list with duplicates, remove all duplicate entries.Assume input list is sorted.
   def remove_duplicates(self):
       curr = self.head
       while curr and curr.next:
          if curr.data == curr.next.data:
             curr.next = curr.next.next
          else:
             curr = curr.next
       return self.head

# ----------------------------------------------------------------------------------------------
# ------------------- >>> H.W <<< --------------------------------

    # H.W // (Reversing a Linked List)
   def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # حفظ المرجع للعقدة التالية
            current.next = prev      # عكس اتجاه المؤشر
            prev = current           # تحريك prev إلى العقدة الحالية
            current = next_node      # تحريك current إلى العقدة التالية
        self.head = prev  


    
    # Another way Using Stack (Reversing a Linked List with Stack)
   def reverse_using_stack(self):
      stack = []
      temp = self.head
      # وضع جميع العقد في المكدس
      while temp:
         stack.append(temp)
         temp = temp.next
      if stack:
         self.head = stack[-1]  # آخر عنصر في المكدس يصبح الرأس
      # إعادة بناء القائمة
      temp = self.head
      stack.pop()
      while stack:
         temp.next = stack.pop()
         temp = temp.next
      temp.next = None

    # Print List
   def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")






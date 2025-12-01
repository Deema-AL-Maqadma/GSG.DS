from AVLNode import AVLNode
# AVL Tree class
class AVLTree:
 
   def get_height(self, node):
       return node.height if node else 0
    
   def get_balance(self, node):
       return self.get_height(node.left) - self.get_height(node.right) if node else 0
 
   def rotate_right(self, y):
       x = y.left
       T2 = x.right
       x.right = y
       y.left = T2
       y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
       x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
       return x
   
   def rotate_left(self, x):
       y = x.right
       T2 = y.left
       y.left = x
       x.right = T2
       x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
       y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
       return y

   def rebalance(self, node):
       balance = self.get_balance(node)
       if balance > 1:
          if self.get_balance(node.left) < 0:
             node.left = self.rotate_left(node.left)
          return self.rotate_right(node)
       if balance < -1:
          if self.get_balance(node.right) > 0:
             node.right = self.rotate_right(node.right)
          return self.rotate_left(node)
       return node
 
   def insert(self, root, key):
       if not root:
           return AVLNode(key)
       elif key < root.key:
           root.left = self.insert(root.left, key)
       else:
           root.right = self.insert(root.right, key)
           root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
       return self.rebalance(root)
   
   def find_min(self, node):
        while node.left:
            node = node.left
        return node

   def delete(self, root, key):
        if not root:
           return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        return self.rebalance(root)


#---------------------------------------------------------------------------------------
# Exercise 1: Validate AVL Tree
   
   def is_avl(self,node):
      if node is None:
         return True

      bf = self.get_balance(node)
      if bf > 1:
          return False

      return self.is_avl(node.left) and self.is_avl(node.right)

#---------------------------------------------------------------------------------------
# Exercise 2: Range Search in AVL Tree
# بترجعهم بترتيب inordr وبتطبعهم
   def range_Search(self,root, low, high):
    if root is None:
        return
    if root.key > low:
        self.range_Search(root.left, low, high)
    if low <= root.key <= high:
        print(root.key)
    if root.key < high:
        self.range_Search(root.right, low, high)
    
    
    #-------------------------------------
    # بترجعهم بليست مرتبة
   def range_sort(self,root, low, high):
    result = []
    if root is None:
        print(result)
        return

    if root.key > low:
        result += self.range_sort(root.left, low, high)

    if low <= root.key <= high:
        result.append(root.value)

    if root.key < high:
        result += self.range_sort(root.right, low, high)

    return result

#---------------------------------------------------------------------------------------
# Exercise 3: Find k-th Smallest Element in AVL Tree
# هيك هترجع العنصر في ال index = key
# لو بدنا يرجع العنصر في الموقع position = key هطرح منه 1 حتى أجيب ال index صح  
   
   def get_indexValue(self,root, key):
    result = []

    if root is None:
        return None

    if root.left:
        result += self.get_indexValue(root.left, key)

    result.append(root.value)

    if root.right:
        result += self.get_indexValue(root.right, key)

    return result[key] if 0 <= key < len(result) else None



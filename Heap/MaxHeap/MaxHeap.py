# MaxHeap Class
class MaxHeap:

    def __init__(self, initial_data=None):
        self.data = []
        if initial_data:
            self.data = list(initial_data)
            self.build_heap()
    
    #---------------------------------------------
    def left_child(self, index):
        return 2 * index + 1

    #---------------------------------------------
    def right_child(self, index):
        return 2 * index + 2

    #---------------------------------------------
    def parent(self, index):
        return (index - 1) // 2

    #---------------------------------------------
    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = self.left_child(index)
            right = self.right_child(index)
            largest = index

            if left < size and self.data[left] > self.data[largest]:
                largest = left
            if right < size and self.data[right] > self.data[largest]:
                largest = right
            if largest == index:
                break

            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            index = largest

    #---------------------------------------------
    def heapify_up(self, index):
        while index > 0:
            parent_index = self.parent(index)
            if self.data[index] > self.data[parent_index]:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    #---------------------------------------------
    def build_heap(self):
        for i in range((len(self.data) - 2) // 2, -1, -1):
            self.heapify_down(i)

    #---------------------------------------------
    def push(self, value):
        self.data.append(value)
        self.heapify_up(len(self.data) - 1)

    #---------------------------------------------
    def peek(self):
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    #---------------------------------------------
    def pop(self):
        if not self.data:
            raise IndexError("pop from empty heap")
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        max_value = self.data.pop()
        if self.data:
            self.heapify_down(0)
        return max_value

    #---------------------------------------------
    def __len__(self):
        return len(self.data)

    #---------------------------------------------
    def __repr__(self):
        return f"MaxHeap({self.data})"
                    
                    
                    
                    
#============================================================
# Deema Mohammed AL-Maqadma
# Heap Assignment
# The Implementation
#============================================================
from MaxHeap import MaxHeap

class MaxHeapDemo:
    def run(self):
        print("---> Build a MaxHeap and Entry Items:")
        values = [10, 4, 15, 20, 8, 7, 25]
        heap = MaxHeap()

        for val in values:
            print(f"Entery: {val}")
            heap.push(val)
            print(heap)

        print("\n============================================\n")
        print("\n---> Poped the items in descending order:")
        while len(heap) > 0:
            max_val = heap.pop()
            print(f"Poped: {max_val}")
            print(heap)

#---------------------------------------------
demo = MaxHeapDemo()
demo.run()
print("\n---> Thx ^_^ <---\n")
                
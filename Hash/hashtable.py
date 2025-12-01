# HashTable class
from node import Node
import math

class HashTable:

    def __init__(self, size, threshold):
        self.size = self._next_prime(size)
        self.threshold = threshold
        self.table = [None] * self.size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def load_factor(self):
        return self.count / self.size

    # ------> Insert <------
    def insert(self, key, value):
        if self.load_factor() > self.threshold:
            self._rehash(self._next_prime(self.size * 2))

        idx = self._hash(key)
        i = 1
        while self.table[idx] is not None and self.table[idx].key != key:
            idx = (self._hash(key) + i * i) % self.size
            i += 1

        self.table[idx] = Node(key, value)
        self.count += 1

    # ------> Search <------
    def search(self, key):
        idx = self._hash(key)
        i = 1
        while self.table[idx] is not None:
            if self.table[idx].key == key:
                return self.table[idx].value
            idx = (self._hash(key) + i * i) % self.size
            i += 1
        return None

    # ------> Delete <------
    def delete(self, key):
        idx = self._hash(key)
        i = 1
        while self.table[idx] is not None:
            if self.table[idx].key == key:
                self.table[idx] = None
                self.count -= 1
                return True
            idx = (self._hash(key) + i * i) % self.size
            i += 1
        return False

    # ------> Rehash <------
    def _rehash(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0
        for node in old_table:
            if node is not None:
                self.insert(node.key, node.value)

    def _is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def _next_prime(self, n):
        while not self._is_prime(n):
            n += 1
        return n
#============================================================
# Deema Mohammed AL-Maqadma
# Hash Assignment
# The Implementation
#============================================================
from hashtable import HashTable

# Usage
# Create a hash table with initial size 7 and load factor threshold 0.7
ht = HashTable(size=7, threshold=0.7)

# Insert key-value pairs into the hash table
for k, v in [(50, 'A'), (700, 'B'), (76, 'C'), (85, 'D'), (92, 'E'), (73, 'F'), (101, 'G')]:
    ht.insert(k, v)

# Search for existing keys
print("---> Search for existing keys:")
print("* 92 ->", ht.search(92))   # Should return 'E'
print("* 76 ->", ht.search(76))   # Should return 'C'

# Delete a key from the hash table
print("\n---> Delete a key from the hash table:")
ht.delete(76)

# Search again after deletion to confirm it's removed
print("---> After deletion, 76 ->", ht.search(76))  # Should return None
print("\n---> Thx^_^ <---\n")
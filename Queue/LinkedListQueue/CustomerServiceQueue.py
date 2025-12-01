# Deema Mohammed AL-Maqadma
# Queue Assignment
# Task: Simulate a basic customer service system using a queue.

from LinledListQueu import LinkedQueue

#--------------------------------------------------------
# Usage

ServiceQueue = LinkedQueue()
ServiceQueue.enqueue("Alice")
ServiceQueue.enqueue("Bob")
ServiceQueue.enqueue("Carol")

# to print all arriving & serving customer
while not ServiceQueue.is_empty():
      current = ServiceQueue.dequeue()
      print(f"Serving: {current}")
print("All customers served.")
print("---> Thx ^_^\n")





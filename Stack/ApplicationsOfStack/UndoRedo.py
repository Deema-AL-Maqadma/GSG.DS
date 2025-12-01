# Undo/Redo in Editors / Web Browser Backtracking
# Two stacks can be used: one for undo, another for redo.

undo_stack = []
redo_stack = []

def perform_action(action):
 undo_stack.append(action)
 redo_stack.clear()

def undo():
 if undo_stack:
   last_action = undo_stack.pop()
   redo_stack.append(last_action)
   print(f"Undo: {last_action}")

def redo():
 if redo_stack:
   last_redo = redo_stack.pop()
   undo_stack.append(last_redo)
   print(f"Redo: {last_redo}")

# Example:
perform_action("Type A")
perform_action("Type B")
undo()
redo()

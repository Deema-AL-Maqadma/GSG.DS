call_stack = []

def call_function(func_name):
   call_stack.append(func_name)
   print(f"Calling: {func_name}")

def return_from_function():
   if call_stack:
       finished = call_stack.pop()
       print(f"Returning from: {finished}")

# Example usage:
call_function("main")
call_function("foo")
return_from_function()
return_from_function()

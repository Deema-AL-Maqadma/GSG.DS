def factorial(n):
   call_stack = []
   result = 1
   
   while n > 1:
      call_stack.append(n)
      n -= 1
   
   while call_stack:
       result *= call_stack.pop()
       return result

# Example usage:
print(factorial(5)) # Output: 120
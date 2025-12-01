# Deema Mohammed AL-Maqadma
# Stack Assignment
# Convert an infix expression to postfix (Reverse Polish Notation)
# The Implementation

#----------------------------------------------------------------------
# To dtermine the priority of operations * / - +
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# #----------------------------------------------------------------------
def infix_to_postfix(expression):
    stack = []  # for storing the operations temporarly
    output = []  # the final result
    
    for char in expression:
        if char.isdigit():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        elif char in "+-*/":
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)

#-----------------------------------------------------------------------
# Usage
expression = "(1+2)*3"
expression = expression.replace(" ", "")  # remove spacing
result = infix_to_postfix(expression)
print()
print("---> Intfix: ", expression)
print("---> Postfix: ", result)
print()
print("Thx ^_^\n")
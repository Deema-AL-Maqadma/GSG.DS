def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():  # إذا كان رقم أو حرف
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # نزيل '(' من الـ stack
        else:  # إذا كان عامل
            while (stack and stack[-1] != '(' and 
                   precedence[char] <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(char)
    
    # إخراج ما تبقى في الـ stack
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)

# اختبار
print(infix_to_postfix("(1 + 2) * 3"))  # Output: "1 2 + 3 *"

# الشرح:
# 1. نستخدم stack لتخزين العوامل والأقواس

# 2. نمر على كل حرف في التعبير:
#    - إذا كان رقم أو متغير نضعه مباشرة في المخرجات
#    - إذا كان '(' نضعه في الـ stack
#    - إذا كان ')' نخرج كل العوامل من الـ stack حتى نصل إلى '('
#    - إذا كان عامل نخرج كل العوامل ذات الأولوية الأعلى أو المتساوية ثم نضع العامل الحالي في الـ stack
# 3. في النهاية نخرج كل ما تبقى في الـ stack
# 4. نرجع النتيجة كسلسلة مفصولة بمسافات

#---------------------------------------------------------------------------------------------------

def infix_to_postfix(expression):
    # تعريف الأولويات لكل عامل
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []      # لتخزين العوامل المؤقتة
    output = []     # لتجميع الناتج النهائي

    # تحويل التعبير إلى قائمة رموز
    tokens = expression.replace('(', ' ( ').replace(')', ') ').split()

    for token in tokens:
        if token.isnumeric():        # إذا كان رقم
            output.append(token)
        elif token == '(':           # إذا فتح قوس
            stack.append(token)
        elif token == ')':           # إذا أغلق قوس
            while stack and stack[-1]!= '(':
                output.append(stack.pop())
            stack.pop()              # إزالة القوس المفتوح
        else:                        # إذا كان عامل (مثل + أو *)
            while stack and stack[-1]!= '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)

    # إخراج كل ما تبقى في الـStack
    while stack:
        output.append(stack.pop())

    return ' '.join(output)


# مثال للتجربة:
expression = "( 1 + 2) * 3"
print("Postfix:", infix_to_postfix(expression))

#----------------------------------------------------------------
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def infix_to_postfix(expression):
    stack = []
    output = []
    
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

# مثال
expr = "(1+2)*3"
expr = expr.replace(" ", "")  # إزالة الفراغات
result = infix_to_postfix(expr)
print("Postfix:", result)
#------------------------------------------------------------------------













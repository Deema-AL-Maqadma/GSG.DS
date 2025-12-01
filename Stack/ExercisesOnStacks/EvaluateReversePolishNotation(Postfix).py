# التمرين 2: تقييم التعبير البولندي العكسي (Postfix)

def eval_rpn(tokens):
    stack = []
    
    for token in tokens:
        if token in "+-*/":  # إذا كان عامل
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # استخدام int للقسمة الصحيحة
        else:  # إذا كان رقم
            stack.append(int(token))
    
    return stack.pop()

# اختبار
print(eval_rpn(["2", "1", "+", "3", "*"]))  # Output: 9
# الشرح:
# 1. نمر على كل عنصر في القائمة
# 2. إذا كان رقم نضعه في الـ stack
# 3. إذا كان عامل نخرج آخر رقمين من الـ stack ونطبق العملية
# 4. نضع النتيجة مرة أخرى في الـ stack
# 5. في النهاية يكون الناتج هو العنصر الوحيد المتبقي في الـ stack

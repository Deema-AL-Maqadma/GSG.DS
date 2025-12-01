# التمرين 3: التحقق من السلسلة المتناظرة (Palindrome)

def is_palindrome(s: str) -> bool:
    stack = []
    length = len(s)
    
    # نضع النصف الأول في الـ stack
    for i in range(length // 2):
        stack.append(s[i])
    
    # نبدأ من المنتصف (نحسب الفرق إذا كانت السلسلة فردية)
    start = length // 2 if length % 2 == 0 else (length // 2) + 1
    
    # نقارن النصف الثاني مع محتويات الـ stack
    for i in range(start, length):
        if stack.pop() != s[i]:
            return False
    
    return True

# اختبار
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

# الشرح:
# 1. نضع النصف الأول من السلسلة في الـ stack
# 2. نبدأ من منتصف السلسلة ونقارن كل حرف مع ما نخرجه من الـ stack
# 3. إذا اختلف أي حرف نرجع False
# 4. إذا انتهينا من المقارنة بنجاح نرجع True

# Answer 1 //
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():  # إذا كان حرف فتح
            stack.append(char)
        elif char in mapping.keys():  # إذا كان حرف غلق
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # أي حرف آخر غير الأقواس
            continue
    
    return not stack  # إذا كانت الستاك فارغة فهي متوازنة

# اختبار
print(is_valid_parentheses("{[()]}"))  # Output: True
print(is_valid_parentheses("{[)]}"))   # Output: False


# ---------------------------------------------------------------------------------




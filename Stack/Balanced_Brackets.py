"""
1. Traverse the expression from left to right.
2. Push each opening bracket onto the stack.
3. For each closing bracket, check if the stack is not empty and the top of the stack is the corresponding opening bracket. If so, pop the stack.
4. If the stack is empty at the end of the traversal, the brackets are balanced.
"""


def is_balanced(expression):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()
    return not stack


expression = "{[()()]}"
print(is_balanced(expression))

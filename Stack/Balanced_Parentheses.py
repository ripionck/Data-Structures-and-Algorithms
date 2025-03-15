"""
balanced parentheses: ((a + b) * c)
unbalanced parentheses: (a + b) * c)

Checking for Balanced Parentheses:
1. When encountering an opening parenthesis (, push it onto the stack.
2. When encountering a closing parenthesis ), check if the stack is not empty and the top of the stack is an opening parenthesis. If so, pop the stack.
3. If the stack is empty at the end of the expression, the parentheses are balanced.

"""


def is_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack


expression = "((a + b) * c)"
print(is_balanced(expression))

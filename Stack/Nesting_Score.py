"""
For each character in the string:
    1. Opening Parenthesis (: Push onto the stack to increase the depth.
    2. Closing Parenthesis ): Add the current depth (length of the stack) to the score and pop from the stack to decrease the depth.
Return the Score: The final score represents the total nesting score.
"""


def nesting_score(s):
    stack = []
    score = 0
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                score += len(stack)
                stack.pop()
    return score


expression = "(()(()))"
print(nesting_score(expression))

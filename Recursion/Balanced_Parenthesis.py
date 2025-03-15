# Iterative approach
"""def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
"""


# Recursive approach
def is_balanced(s):
    def check_balance(index, balance):
        if balance < 0:
            return False
        if index == len(s):
            return balance == 0
        if s[index] == '(':
            return check_balance(index+1, balance+1)
        elif s[index] == ')':
            return check_balance(index+1, balance-1)
        else:
            return check_balance(index+1, balance)
    return check_balance(0, 0)


string = "(())("
print(is_balanced(string))

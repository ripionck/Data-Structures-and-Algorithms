# GCD --> Greatest Common Divisor
# Iterative approach
"""def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
"""


# Recursive approach
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = 48
num2 = 18
print(gcd(num1, num2))

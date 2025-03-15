# Iterative approach
"""def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
"""


# Recursive approach
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)


base = 2
exponent = 4
print(power(base, exponent))

# Iterative approach
"""def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
"""


# Recursive approach
def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n-1)


n = 10
print(sum(n))

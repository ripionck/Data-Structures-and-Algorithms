# Iterative approach
"""
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary
"""


#  Recursive approach
def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n//2) + str(n % 2)


decimal_number = 11
print(decimal_to_binary(decimal_number))

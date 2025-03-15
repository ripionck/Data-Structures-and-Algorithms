# Iterative approach
"""def square_num(n):
    return n*n
"""


# Iterative approach
def square_num(n):
    if n == 0:
        return 0
    return square_num(n-1) + n + n-1


# square_num(4) = square_num(3) + 4 + 3
#                = (square_num(2) + 3 + 2) + 4 + 3
#                = ((square_num(1) + 2 + 1) + 3 + 2) + 4 + 3
#                = (((square_num(0) + 1 + 0) + 2 + 1) + 3 + 2) + 4 + 3
#                = (((0 + 1 + 0) + 2 + 1) + 3 + 2) + 4 + 3
#                = ((1 + 2 + 1) + 3 + 2) + 4 + 3
#                = (4 + 3 + 2) + 4 + 3
#                = 9 + 4 + 3
#                = 16


number = 4
print(square_num(number))

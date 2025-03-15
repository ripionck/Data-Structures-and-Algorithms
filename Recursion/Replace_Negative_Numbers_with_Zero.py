# Iterative approach
"""def replace_negative_numbers(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0
    return lst
"""


# Recursive approach
def replace_negative_numbers(lst, index=0):
    if index == len(lst):
        return lst
    if lst[index] < 0:
        lst[index] = 0
    return replace_negative_numbers(lst, index+1)


numbers = [1, -2, 3, -4, 5]
print(replace_negative_numbers(numbers))

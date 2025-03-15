# Iterative approach
"""def find_first_occurence(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1  # return -1 if the target is not found
"""


# Recursive approach
def find_first_occurence(lst, target, index=0):
    if index >= len(lst):
        return -1
    if lst[index] == target:
        return index
    return find_first_occurence(lst, target, index+1)


numbers = [4, 2, 7, 3, 7, 1]
target = 7
print(find_first_occurence(numbers, target))

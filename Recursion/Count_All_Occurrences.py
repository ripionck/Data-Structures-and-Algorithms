# Iterative approach
"""def count_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count
"""

# Recursive approach


def count_occurrences(lst, target):
    if not lst:
        return 0
    return (1 if lst[0] == target else 0) + count_occurrences(lst[1:], target)


numbers = [1, 2, 3, 4, 2, 2, 5]
target_num = 2
print(count_occurrences(numbers, target_num))

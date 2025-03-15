"""
Time complexity -----> O(n)
"""


def second_maximum(nums):
    if len(nums) < 2:
        return None  # Return None if the list has fewer than 2 element

    max_value = second_max = float('-inf')

    for num in nums:
        if num > max_value:
            second_max = max_value
            max_value = num
        elif num > second_max and num < max_value:
            second_max = num

    return second_max if second_max != float('-inf') else None


"""
Time complexity -----> O(n log n)
"""


def second_maximum(nums):
    if len(nums) < 2:
        return None
    unique_sorted = sorted(set(nums), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None


nums = [10, 5, 8, 12, 3, 7, 1, 9]
second_max = second_maximum(nums)
print(second_max)

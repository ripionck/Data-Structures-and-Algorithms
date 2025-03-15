"""
Time complexity ----> O(n)
"""


def find_minimum(nums):
    if not nums:
        return None

    minimum = nums[0]  # Start with the first element as the minimum
    for num in nums[1:]:
        if num < minimum:
            minimum = num
    return minimum


"""def find_minimum(nums):
    if not nums:
        return None  # Return None for an empty list
    return min(nums)
"""


my_list = [10, 5, 2, 8, 3, 7, 1, 9]
minimum = find_minimum(my_list)
print(minimum)

# Iterative approach
"""def average(nums):
    if not nums:
        return 0
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
"""


# Recursive approach
def nums_sum(nums, index=0):
    if index == len(nums):
        return 0
    return nums[index] + nums_sum(nums, index+1)


def average(nums):
    if not nums:
        return 0
    total = nums_sum(nums)
    return total / len(nums)


numbers = [1, 2, 3, 4, 5]
print(average(numbers))

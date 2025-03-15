"""
This problem requires calculating the product of all elements in an array except the current element, without using division.

arr = [1, 2, 3, 4]
output = [24, 12, 8, 6]
24 = 2*3*4
12 = 1*3*4
8 = 1*2*4
6 = 1*2*3

Time complexity ----> O(n)
Space complexity -----> O(1)
"""


def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products and combine
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


nums = [1, 2, 3, 4]
result = product_except_self(nums)
# print(result)

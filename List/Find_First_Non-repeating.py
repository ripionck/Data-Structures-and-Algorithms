def first_non_repeating(nums):
    # Count frequency of each number
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Find first number with count 1
    for num in nums:
        if count[num] == 1:
            return num

    return None  # If no non-repeating element found


nums = [2, 3, 2, 4, 3, 5, 6, 5]
result = first_non_repeating(nums)
print(result)

"""
using hash table approach
Time complexity ----> O(n)
Space complexity ----> O(n)
"""

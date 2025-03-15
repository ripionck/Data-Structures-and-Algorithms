"""
Using Brute Force 
Time complexity -----> O(n²)
Space complexity -----> O(1)
Not efficient for large list
"""


def find_two_numbers(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == k:
                return [nums[i], nums[j]]

    return []  # If no solution is found


"""
Using Hash Table
Time complexity -----> O(n)
Space complexity -----> O(n)
Best for unsorted list
"""


def find_two_numbers(nums, k):
    seen = {}
    for num in nums:
        complement = k - num
        if complement in seen:
            return [complement, num]
        seen[num] = True
    return []


"""
Using Two Pointers Technique
Time complexity -----> O(nlogn)
Space complexity ------> O(1)
Good when list is already sorted

"""


def find_two_numbers(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == k:
            return [nums[left], nums[right]]
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    return []


nums = [1, 4, 45, 6, 10, -8]
k = 16

result = find_two_numbers(nums, k)
print(result)

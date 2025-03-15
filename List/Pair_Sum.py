# Time -----> O(n*n)
"""def pair_sum(numbers, target_sum):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return (i, j)
"""

# Time ------> O(n)


def pair_sum(numbers, target_sum):
    previous_nums = {}

    for index, num in enumerate(numbers):
        complement = target_sum - num

        if complement in previous_nums:
            return (previous_nums[complement], index)

        previous_nums[num] = index


print(pair_sum([3, 2, 5, 6, 1], 8))

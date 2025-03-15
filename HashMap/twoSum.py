def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
        
        
nums = [2, 4, 5, 7, 9, 11]
target = 13
print(twoSum(nums, 13))
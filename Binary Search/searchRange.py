def searchRangeLinear(nums, target):
    first_position = -1
    last_position = -1
    
    for i in range(len(nums)):
        if nums[i] == target:
            if first_position == -1:
                first_position = i
            last_position = i

    return [first_position, last_position]

def searchRangeBinary(nums, target):
    def findFirst(nums, target):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
                
        if start < len(nums) and nums[start] == target:
            return start
        return -1
    
    def findLast(nums, target):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        
        if end >= 0 and nums[end] == target:
            return end
        return -1
    
    return [findFirst(nums, target), findLast(nums, target)]

nums = [5,7,7,8,8,10]
target = 8

print(searchRangeLinear(nums, target))
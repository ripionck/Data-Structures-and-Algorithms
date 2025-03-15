
def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
    return start
        

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))
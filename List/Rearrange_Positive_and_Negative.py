def rearrange_positive_negative(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        # Move left pointer right until we find a negative number
        while left < len(nums) and nums[left] >= 0:
            left += 1

        # move right pointer left until we find a positive number
        while right >= 0 and nums[right] <= 0:
            right -= 1

        # If pointers haven't crossed, swap the elements
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    return nums


lst = [1, -2, 3, 4, -5, 6, -7, 8, -9, 10]
print(rearrange_positive_negative(lst))

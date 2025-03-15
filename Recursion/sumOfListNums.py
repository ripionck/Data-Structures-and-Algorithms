def sumOfListNums(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum(list[1:])
    
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sumOfListNums(nums))
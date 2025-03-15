def rotate_list(lst, k):
    if not lst:
        return lst

    k = k % len(lst)  # Handle cases where k > len(lst)
    return lst[-k:] + lst[:-k]


my_list = [1, 2, 3, 4, 5]
rotated = rotate_list(my_list, 2)
print(rotated)


"""
Time complexity ------> O(n)
Space complexity -------> O(n)
"""

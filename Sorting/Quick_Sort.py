def partition(array, start, end):

    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:  # moving high towards left
            high = high - 1

        while low <= high and array[low] <= pivot:  # moving low towards right
            low = low + 1

        if low <= high:  # checking if low and high have crossed
            array[low], array[high] = array[high], array[low]

        else:
            break     # breaking out of the loop if low > high

    # swapping pivot with high so that pivot is at its right # #position
    array[start], array[high] = array[high], array[start]

    return high  # returning pivot position


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [5, 1, 3, 9, 8, 2, 7]

quick_sort(array, 0, len(array) - 1)
print(array)

# worst-case time complexity ---> O(n2)
# average-case time complexity ---->  O(n logn)
# Space Complexity: O(logn) for the in-place version, O(n) for the version using extra lists.

"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr))
"""

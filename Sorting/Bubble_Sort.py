# Iterative 1
"""def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
"""


# Iterative 2
"""def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        exchanges = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                exchanges = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not exchanges:
            break
"""


# Iterative 3
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swap was made
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break


# Recursive
"""def bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    # If array size is 1, return
    if n == 1:
        return
    # One pass of bubble sort. After this pass, the largest element is moved to the end
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    # largest element is fixed, recur for remaining array
    bubble_sort(arr, n-1)
"""

array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(array)
print(array)

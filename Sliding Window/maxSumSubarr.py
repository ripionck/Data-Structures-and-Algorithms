def max_sum_subarray(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum of a subarray of size {}: {}".format(k, max_sum_subarray(arr, k)))

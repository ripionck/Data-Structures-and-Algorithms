def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Add remaining elements from list1, if any
    merged.extend(list1[i:])

    # Add remaining elements from list2, if any
    merged.extend(list2[j:])

    return merged


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
result = merge_sorted_lists(list1, list2)
print(result)

"""
Time complexity ----> O(n+m), where n and m are the lenghts of the input lists
Space complexity ----> O(n+m)
"""

import heapq

# Create a list with negated values for max-heap
max_heap = [-21, -1, -45, -78, -3, -5]

# Convert to a max-heap
heapq.heapify(max_heap)
print("Max-Heap:", [-x for x in max_heap]) # Output: [78, 45, 21, 1, 3, 5]

# Add an element to the max-heap
heapq.heappush(max_heap, -8)
print("After push:", [-x for x in max_heap]) # Output: [78, 45, 21, 8, 3, 5]

# Remove the largest element
largest = -heapq.heappop(max_heap)
print("Popped element:", largest)          # Output: 78
print("Max-Heap after pop:", [-x for x in max_heap]) # Output: [45, 8, 21, 1, 3]

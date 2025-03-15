import heapq

# Create a list
heap = [21, 1, 45, 78, 3, 5]

# Convert the list into a heap
heapq.heapify(heap)
print("Heap:", heap)  # Output: [1, 3, 5, 78, 21, 45]

# Add an element to the heap
heapq.heappush(heap, 8)
print("After push:", heap)  # Output: [1, 3, 5, 78, 21, 45, 8]

# Remove the smallest element
smallest = heapq.heappop(heap)
print("Popped element:", smallest)  # Output: 1
print("Heap after pop:", heap)      # Output: [3, 8, 5, 78, 21, 45]

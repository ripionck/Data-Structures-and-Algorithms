A **deque** (short for "double-ended queue") is an abstract data type that allows insertion and deletion of elements from both ends—front and rear. It combines the properties of stacks and queues, making it a versatile linear data structure.

## Key Features of Deque

- **Bidirectional Operations**: Elements can be added or removed from both the front and rear.
- **Dynamic Size**: The size of a deque can grow or shrink dynamically as elements are added or removed.
- **Efficient Operations**: Adding or removing elements at either end is typically **O(1)**, depending on the implementation.

## Operations in Deque

1. **Initialization**: `Deque()` creates an empty deque.
2. **Additions**:
   - `add_front(item)`: Adds an item to the front.
   - `add_rear(item)`: Adds an item to the rear.
3. **Removals**:
   - `remove_front()`: Removes and returns the front item.
   - `remove_rear()`: Removes and returns the rear item.
4. **Utility Functions**:
   - `is_empty()`: Checks if the deque is empty.
   - `size()`: Returns the number of items in the deque.

## Representation of Deque

### 1. **Array-Based Representation**

- A deque can be implemented using a fixed-size array or a dynamic array.
- Two pointers, `front` and `rear`, are used to track the ends of the deque.
- In a circular array implementation, when either pointer reaches the end, it wraps around to the beginning.

### 2. **Linked List Representation**

- A doubly linked list is often used for deques, where each node has pointers to both its previous and next nodes.
- This allows efficient insertion and deletion at both ends.

### Example Representation Using Circular Queue:

| Operation      | Front Pointer | Rear Pointer | Deque Contents   |
| -------------- | ------------- | ------------ | ---------------- |
| Initial State  | -1            | -1           | []               |
| Add Rear (5)   | 0             | 0            | [5]              |
| Add Front (10) | MAXSIZE-1     | 0            | [10, _, _, _, 5] |
| Remove Front   | 0             | 0            | [_, _, _, _, 5]  |

## Python Example Implementation

```python
class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Example usage
d = Deque()
d.add_rear(5)
d.add_front(10)
print(d.remove_front())  # Output: 10
print(d.size())          # Output: 1
```

## Applications of Deque

- **Sliding Window Problems**: Efficiently manage a moving subset of elements.
- **Palindrome Checking**: Compare elements from both ends.
- **Undo/Redo Operations**: Maintain history in applications.

Deques are highly flexible and efficient for scenarios requiring frequent additions and removals at both ends.

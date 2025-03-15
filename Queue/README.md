A **queue** is a linear data structure that operates on the **First-In-First-Out (FIFO)** principle. This means that the first element added to the queue is the first one to be removed, similar to people standing in line for a service.

## Key Characteristics of a Queue

- **FIFO Principle**: The first element inserted is the first one removed.
- **Two Pointers**:
  - `Front`: Tracks the element to be removed.
  - `Rear`: Tracks where new elements are added.
- **Basic Operations**:
  - **Enqueue**: Add an element at the rear.
  - **Dequeue**: Remove an element from the front.
  - **Peek**: Retrieve the front element without removing it.
  - **isEmpty**: Check if the queue is empty.
  - **isFull**: Check if the queue is full.

## Representation of a Queue

A queue can be implemented using:

1. **Arrays**: A simple and fixed-size implementation.
2. **Linked Lists**: A dynamic implementation where elements are connected via pointers.
3. **Pointers and Structures**: For more advanced use cases.

### Array Representation

In an array-based queue:

- The `front` and `rear` pointers are initialized to `-1`.
- During `enqueue`, the `rear` pointer increments, and the new element is added at this position.
- During `dequeue`, the `front` pointer increments, effectively removing the front element.

### Linked List Representation

In a linked list-based queue:

- Each node contains data and a pointer to the next node.
- The `front` points to the first node, while the `rear` points to the last node.

## Operations in Detail

1. **Enqueue (Insertion)**:

   - Check if the queue is full (for arrays).
   - Increment the `rear` pointer and add the new element.
   - If it's the first element, set both `front` and `rear` to 0.

2. **Dequeue (Deletion)**:

   - Check if the queue is empty.
   - Remove and return the element at `front`.
   - Increment the `front` pointer. If it exceeds `rear`, reset both pointers to `-1`.

3. **Peek**:

   - Return the value at `front` without modifying it.

4. **isEmpty & isFull**:
   - For arrays, check conditions based on pointer positions.

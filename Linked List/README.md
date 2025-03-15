## Linked List Data Structure: Explanation and Representation

A **linked list** is a linear data structure where elements, called _nodes_, are connected through pointers. Unlike arrays, linked lists do not require contiguous memory allocation, making them dynamic and flexible in size. Each node typically consists of two components:

1. **Data**: The value stored in the node.
2. **Pointer**: A reference to the next node in the sequence.

The last node in a linked list points to `NULL`, indicating the end of the list.

### Key Characteristics

- Nodes can be stored anywhere in memory, unlike arrays, which require contiguous memory.
- Efficient insertion and deletion operations, as no shifting is needed.
- Traversal requires visiting nodes sequentially, making random access slower compared to arrays.

---

### Representation of Linked Lists

A linked list is visually represented as follows:

```
[Data | Pointer] -> [Data | Pointer] -> [Data | NULL]
```

- The **head** pointer stores the address of the first node.
- Each node's pointer field links to the next node.
- The last node's pointer field contains `NULL`.

---

### Types of Linked Lists

1. **Singly Linked List**:

   - Each node points to its next node.
   - Traversal is unidirectional (forward only).
   - Example:
     ```
     Head -> [Data | Pointer] -> [Data | NULL]
     ```

2. **Doubly Linked List**:

   - Each node has two pointers: one pointing to the previous node and one to the next.
   - Traversal is bidirectional (forward and backward).
   - Example:
     ```
     NULL  [Prev | Data | Next] -> NULL
     ```

3. **Circular Linked List**:
   - The last node points back to the first node, forming a loop.
   - Can be singly or doubly linked.
   - Example:
     ```
     Head -> [Data | Pointer] -> [Data | Pointer] -> Head
     ```

---

### Advantages of Linked Lists

- Dynamic memory allocation allows resizing without wasting space.
- Efficient insertion/deletion at any position (O(1) for head/tail).
- Suitable for applications requiring frequent modifications, such as dynamic queues or stacks.

Linked lists are widely used in scenarios like managing browser history, implementing graphs, or simulating circular processes (e.g., round-robin scheduling).

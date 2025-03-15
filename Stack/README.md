## Stack Data Structure Explained

A stack is a linear data structure that operates on the **Last In First Out (LIFO)** principle. This means that the last element added to the stack is the first one to be removed. It is commonly visualized as a stack of plates or books, where only the top item can be accessed or removed.

### Key Operations of a Stack

1. **Push**: Adds an element to the top of the stack.
2. **Pop**: Removes and returns the top element of the stack.
3. **Peek**: Returns the top element without removing it.
4. **isEmpty**: Checks if the stack is empty.
5. **Size**: Returns the number of elements in the stack.

### Representation of a Stack

Stacks can be represented using:

- **Arrays**: Fixed size stacks where elements are stored sequentially.
- **Linked Lists**: Dynamic stacks where each element points to the next.

#### Example Representation Using Array

- A pointer `TOP` tracks the topmost element.
- Initially, `TOP = -1` indicates an empty stack.
- On `push`, `TOP` increments, and the new element is added at `arr[TOP]`.
- On `pop`, the element at `arr[TOP]` is returned, and `TOP` decrements.

#### Example Representation Using Linked List

- Each node contains a value and a pointer to the next node.
- The `TOP` pointer refers to the last inserted node.

### Applications of Stack

Stacks are widely used in:

- Expression evaluation and conversion (e.g., infix to postfix).
- Parentheses matching in expressions.
- Function call management (e.g., recursion).
- Undo operations in editors.
- Memory management and backtracking algorithms (e.g., Tower of Hanoi)[1][5][6].

### Visual Representation

Imagine a stack of plates:

1. You can only add or remove plates from the top.
2. Removing plates follows LIFO—last plate added is removed first.

This analogy demonstrates how stacks work in real-world scenarios.

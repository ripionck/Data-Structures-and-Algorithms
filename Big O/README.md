# Big O Notation Cheat Sheet

## Common Time Complexities

- **O(1)** Constant

  - No loops
  - Example: Accessing a specific element in an array

- **O(log n)** Logarithmic

  - Usually searching algorithms on sorted data
  - Example: Binary search

- **O(n)** Linear

  - Single loops iterating through n items
  - Example: Linear search
  - _Note:_ Iterating through half a collection is still O(n)

- **O(n log n)** Log Linear

  - Typically sorting operations
  - Example: Merge sort, Quick sort

- **O(n²)** Quadratic

  - Nested loops where each element is compared to every other element
  - Example: Bubble sort, Insertion sort

- **O(2ⁿ)** Exponential

  - Recursive algorithms that solve a problem of size N by recursively solving two smaller problems of size N-1
  - Example: Naive recursive Fibonacci

- **O(n!)** Factorial
  - Adding a loop for every element
  - Example: Permutations of a string

## Important Notes

- For two separate collections of size a and b:
  - Nested operations become **O(a \* b)**
  - Non-nested operations become **O(a + b)**

| Big O      | Name         | Description                                     |
| ---------- | ------------ | ----------------------------------------------- |
| O(1)       | Constant     | Statement, one line of code                     |
| O(log n)   | Logarithmic  | Divide and conquer (binary search)              |
| O(n)       | Linear       | Loop                                            |
| O(n log n) | Linearithmic | Effective sorting algorithms                    |
| O(n²)      | Quadratic    | Double loop                                     |
| O(n³)      | Cubic        | Triple loop                                     |
| O(2ⁿ)      | Exponential  | Complex full search (recursive Fibonacci, etc.) |

| Operation Type             | Examples                          | Time Impact         |
| -------------------------- | --------------------------------- | ------------------- |
| **Arithmetic Operations**  | `+`, `-`, `*`, `/`, `%`           | O(1)                |
| **Comparisons**            | `==`, `===`, `<`, `>`, `<=`, `>=` | O(1)                |
| **Looping**                | `for`, `while`, `forEach`, `map`  | O(n) or higher      |
| **Function Calls**         | `myFunction()`, `external.call()` | Depends on function |
| **Logarithmic Operations** | Binary search, divide-and-conquer | O(log n)            |

## Sorting Algorithms

| Algorithm          | Space Complexity | Time Complexity (Best) | Time Complexity (Worst) |
| ------------------ | ---------------- | ---------------------- | ----------------------- |
| **Insertion Sort** | O(1)             | O(n)                   | O(n²)                   |
| **Selection Sort** | O(1)             | O(n²)                  | O(n²)                   |
| **Bubble Sort**    | O(1)             | O(n)                   | O(n²)                   |
| **Merge Sort**     | O(n)             | O(n log n)             | O(n log n)              |
| **Quick Sort**     | O(log n)         | O(n log n)             | O(n²)                   |
| **Heap Sort**      | O(1)             | O(n log n)             | O(n log n)              |

## Common Data Structure Operations

| Data Structure         | Access (Worst) | Search (Worst) | Insertion (Worst) | Deletion (Worst) | Space Complexity |
| ---------------------- | -------------- | -------------- | ----------------- | ---------------- | ---------------- |
| **Array**              | O(1)           | O(n)           | O(n)              | O(n)             | O(n)             |
| **Stack**              | O(n)           | O(n)           | O(1)              | O(1)             | O(n)             |
| **Queue**              | O(n)           | O(n)           | O(1)              | O(1)             | O(n)             |
| **Singly-Linked List** | O(n)           | O(n)           | O(1)              | O(1)             | O(n)             |
| **Doubly-Linked List** | O(n)           | O(n)           | O(1)              | O(1)             | O(n)             |
| **Hash Table**         | N/A            | O(n)           | O(n)              | O(n)             | O(n)             |

_Note:_

- Hash table complexities assume poor hash function leading to many collisions
- Stack/Queue complexities assume array implementation (pointer-based would have O(n) access/search)
- Linked list insertion/deletion assumes operation at known position (O(n) if need to search first)

Here's a comprehensive **Big O Rule Book** for your README.md, formatted with clear explanations and examples:

````markdown
# Big O Rule Book

## Time Complexity Rules

### 🔴 Rule 1: Always Worst Case

Always analyze the worst-case scenario for algorithms.

```python
# Example: Linear search
# Best: O(1) (first element), Worst: O(n) -> We use O(n)
```
````

### 🔴 Rule 2: Remove Constants

Drop constant factors and lower-order terms.

```python
# O(2n + 100) → O(n)
# O(50) → O(1)
```

### 🔴 Rule 3: Different Inputs, Different Variables

- **Sequential operations**: O(a + b)
  ```python
  # Processing two separate arrays
  for x in array1: ... # O(a)
  for y in array2: ... # O(b)
  ```
- **Nested operations**: O(a \* b)
  ```python
  # Nested loops with different inputs
  for x in array1:       # O(a)
    for y in array2: ... # O(b)
  ```

### 🔴 Rule 4: Drop Non-Dominant Terms

Keep only the most significant term.

```python
# O(n² + n + log n) → O(n²)
# O(n! + 3^n + n^3) → O(n!)
```

---

## Space Complexity Rules

### What Contributes to Space Complexity?

| Factor              | Examples                     |
| ------------------- | ---------------------------- |
| **Variables**       | `x = 5`, `temp = []`         |
| **Data Structures** | Arrays, Hash Tables, Objects |
| **Function Calls**  | Recursion call stack         |
| **Allocations**     | New objects/arrays created   |

### Key Principles:

1. **Input space isn't counted** (only auxiliary space)
2. **Recursion depth matters** (each call adds to stack)
3. **Temporary storage counts**

```python
# O(n) space example
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)  # n stack frames
```

---

## Must-Know Additions

### ⚡ Rule 5: Recursion Complexity

- **Time**: Number of calls × Work per call
- **Space**: Maximum call stack depth

```python
# Fibonacci (naive)
# Time: O(2^n), Space: O(n)
```

### ⚡ Rule 6: Amortized Time

Some operations may occasionally be expensive, but average over time is better.

```python
# Dynamic array resizing
# Single insertion: O(n) when resizing, but O(1) amortized
```

### ⚡ Rule 7: Logarithmic Cases

- Halving/doubling patterns → O(log n)
- Binary search, balanced trees, etc.

---

## Cheat Sheet

| Pattern                 | Time              | Space    |
| ----------------------- | ----------------- | -------- |
| Single loop             | O(n)              | O(1)     |
| Nested loops            | O(n²)             | O(1)     |
| Divide & conquer        | O(log n)          | O(log n) |
| Recursion (brute force) | O(branches^depth) | O(depth) |

```

```

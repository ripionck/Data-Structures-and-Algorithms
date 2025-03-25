## 1. What is Recursion?

A function that calls itself until a **base condition** is met. Contains:

- **Base Case**: Stopping condition
- **Recursive Case**: Function calling itself

```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n-1)
```

## 2. How Recursion Works (Visual Representation)

**Example: factorial(5)**

```python
factorial(5)
5 * factorial(4)
    4 * factorial(3)
        3 * factorial(2)
            2 * factorial(1)
                1 * factorial(0)
                    return 1  # Base case reached
                return 1*1 = 1
            return 2*1 = 2
        return 3*2 = 6
    return 4*6 = 24
return 5*24 = 120
```

## 3. Key Concepts to Know

### a. Call Stack Visualization

Each recursive call creates a new stack frame:

| Stack Frame  | Value | State     |
| ------------ | ----- | --------- |
| factorial(5) | 5\*24 | Waiting   |
| factorial(4) | 4\*6  | Waiting   |
| factorial(3) | 3\*2  | Waiting   |
| factorial(2) | 2\*1  | Waiting   |
| factorial(1) | 1\*1  | Waiting   |
| factorial(0) | 1     | Completed |

### b. Base Case Requirements

Essential to prevent infinite recursion:

```python
# Bad example (missing base case)
def infinite_recursion():
    infinite_recursion()  # Crash: RecursionError
```

### c. Recursion vs Iteration

Choose recursion when:

- Problem has natural recursive structure (trees, divide-and-conquer)
- Code clarity is more important than performance

## 4. Common Recursion Patterns

### Pattern 1: Direct Recursion

```python
def count_down(n):
    if n < 0: return
    print(n)
    count_down(n-1)
```

### Pattern 2: Tree Recursion (Fibonacci)

```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)  # Two recursive calls
```

### Pattern 3: Tail Recursion

(Note: Python doesn't optimize tail recursion)

```python
def factorial_tail(n, accumulator=1):
    if n == 0: return accumulator
    return factorial_tail(n-1, n*accumulator)
```

## 5. Important Considerations

### a. Stack Overflow

Python has recursion depth limit (~1000):

```python
def cause_overflow():
    cause_overflow()  # RecursionError: maximum depth exceeded
```

### b. Memoization Optimization

For overlapping subproblems (Fibonacci):

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

### c. Recursion Depth

Check with:

```python
import sys
print(sys.getrecursionlimit())  # Default: 1000
```

## 6. Practical Examples

### Example 1: Binary Search

```python
def binary_search(arr, target, low=0, high=None):
    if high is None: high = len(arr) - 1
    if low > high: return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, high)
    else:
        return binary_search(arr, target, low, mid-1)
```

### Example 2: Directory Traversal

```python
import os

def list_files(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            list_files(full_path)  # Recursive call
        else:
            print(full_path)
```

## 7. Recursion Checklist

1. Always define base case(s) first
2. Ensure progress toward base case
3. Consider stack depth limitations
4. Watch for repeated computations (use memoization)
5. Test edge cases (0, 1, empty input)
6. Consider iterative alternatives for performance

## 8. When to Use Recursion

- **Good For**: Tree traversals, backtracking, divide-and-conquer
- **Avoid When**: Deep recursion needed, performance-critical code

Recursion can create elegant solutions for problems with recursive structure, but always consider Python's recursion limits and potential memory implications.

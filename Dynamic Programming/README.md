**Dynamic programming (DP)** is a computational technique that optimizes recursive problems by breaking them into overlapping subproblems, solving each only once, and storing their solutions for future reference. This approach dramatically improves efficiency by avoiding redundant calculations, particularly in problems exhibiting **optimal substructure** (solutions depend on optimal sub-solutions) and **overlapping subproblems**.

---

### Key Components of Dynamic Programming

1. **Memoization (Top-Down)**:  
   Stores results of subproblems in a lookup table (e.g., hashmap or array) to avoid recomputation.  
   Example for Fibonacci numbers:

   ```python
   memo = {0: 0, 1: 1}
   def fib(n):
       if n not in memo:
           memo[n] = fib(n-1) + fib(n-2)
       return memo[n]
   ```

   Here, `fib(5)` computes `fib(4)` and `fib(3)`, reusing stored values for smaller `n`.

2. **Tabulation (Bottom-Up)**:  
   Builds solutions iteratively from the smallest subproblems.  
   Example:
   ```python
   def fib(n):
       if n == 0: return 0
       prev, curr = 0, 1
       for _ in range(n-1):
           prev, curr = curr, prev + curr
       return curr
   ```
   This avoids recursion overhead by iterating from `fib(0)` to `fib(n)`.

---

### Example: Fibonacci Sequence

The Fibonacci sequence **F(n) = F(n-1) + F(n-2)** illustrates DP’s efficiency:

- **Naive Recursion**: Exponential time (**O(2^n)**) due to redundant calls.
- **DP Approach**: Linear time (**O(n)**) and space by storing results.

| Step | Subproblems Solved | Result Stored |
| ---- | ------------------ | ------------- |
| F(0) | Base case          | 0             |
| F(1) | Base case          | 1             |
| F(2) | F(1) + F(0)        | 1             |
| F(3) | F(2) + F(1)        | 2             |
| F(4) | F(3) + F(2)        | 3             |

---

### When to Use Dynamic Programming

- **Overlapping Subproblems**: Repeated calculations for the same inputs (e.g., Fibonacci, shortest path problems).
- **Optimal Substructure**: Overall optimal solution can be constructed from optimal solutions to subproblems (e.g., knapsack problem).

---

### DP vs. Other Techniques

| Approach                | Pros                  | Cons                           |
| ----------------------- | --------------------- | ------------------------------ |
| **Recursion**           | Simple implementation | Redundant computations         |
| **Greedy Methods**      | Fast, low complexity  | No guarantee of global optimum |
| **Dynamic Programming** | Guarantees optimality | Higher memory usage            |

---

### Representation in Practice

DP problems are often represented using:

- **State Transition Equations**: Define how subproblems relate (e.g., ** F(n) = F(n-1) + F(n-2) **)[1][2].
- **DP Tables/Arrays**: Store solutions to subproblems (e.g., `dp[i] = dp[i-1] + dp[i-2]`).

By leveraging these representations, DP transforms intractable problems into efficient, solvable ones.

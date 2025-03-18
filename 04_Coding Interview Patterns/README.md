## Coding Interview Patterns, Alex Xu

### Notes

<!-- TOC -->

- [Char 1 Two Pointers](#char-1-two-pointers)
  - [Pair Sum - Sorted](#pair-sum---sorted)
  - [Triplet Sum](#triplet-sum)
  - [palindrome valid](#palindrome-valid)
  - [largest container](#largest-container)
  - [Shift Zeros to the End](#shift-zeros-to-the-end)
  - [Next Lexicographical Sequence](#next-lexicographical-sequence)
- [Char 2 Hash Map](#char-2-hash-map)
  - [Pair Sum Unsorted](#pair-sum-unsorted)
  - [Verify Sudoku Board](#verify-sudoku-board)
  - [Zero stripping](#zero-stripping)
  - [Longest Chain of Consecutive Numbers](#longest-chain-of-consecutive-numbers)
  - [Geometric Sequence Triplets](#geometric-sequence-triplets)
- [Char 3 Linked List](#char-3-linked-list)
  - [remove k-th last node](#remove-k-th-last-node)
  - [linked list intersection](#linked-list-intersection)
  - [LRU cache](#lru-cache)
  - [Palindromic Linked List](#palindromic-linked-list)
  - [Flatten a Multi-Level Linked List](#flatten-a-multi-level-linked-list)
- [Char 4 Fast Slow Pointers](#char-4-fast-slow-pointers)
  - [Linked List Loop](#linked-list-loop)
  - [Linked List Midpoint](#linked-list-midpoint)
  - [Happy Number](#happy-number)
- [Char 5 Sliding Windows](#char-5-sliding-windows)
  - [Substring Anagrams](#substring-anagrams)
  - [Longest substring with unique characters](#longest-substring-with-unique-characters)
  - [optimized](#optimized)
  - [Longest Uniform substring after replacement](#longest-uniform-substring-after-replacement)
- [Char 6 Binary Search](#char-6-binary-search)
  - [Find Insertion Index](#find-insertion-index)
  - [First and Last Occurrence of Number](#first-and-last-occurrence-of-number)
  - [Cutting Wood](#cutting-wood)
- [Determine if the current value of H cuts at least k meters of wood](#determine-if-current-value-of-h-cuts-at-least-k-meters-of-wood)
  - [Find target in rotated sorted array](#find-target-in-rotated-sorted-array)
  - [Find Median From Two Sorted Arrays](#find-median-from-two-sorted-arrays)
  - [Matrix Search](#matrix-search)
  - [Local Maxima in Array](#local-maxima-in-array)
  - [Weighted Random Selection](#weighted-random-selection)
- [Char 7 Stack](#char-7-stack)
  - [Valid Parenthesis Expression](#valid-parenthesis-expression)
  - [Next Largest Number to the Right](#next-largest-number-to-the-right)
  - [Evaluate Expression](#evaluate-expression)
  - [Repeated Removal of Adjacent Duplicates](#repeated-removal-of-adjacent-duplicates)
  - [Implement Queue Using Stacks](#implement-queue-using-stacks)
  - [Max of Sliding Window](#max-of-sliding-window)
- [Char 8 Heaps](#char-8-heaps)
  - [K most frequent strings](#k-most-frequent-strings)
  - [Max Heap](#max-heap)
  - [Min Heap](#min-heap)
  - [Combine Sorted linked lists](#combine-sorted-linked-lists)
  - [Median of Integer Stream](#median-of-integer-stream)
  - [Sort K-Sorted Array](#sort-k-sorted-array)
- [Char 9 Interval](#char-9-interval)
  - [Merge Overlapping Intervals](#merge-overlapping-intervals)
  - [Identify All Interval Overlaps](#identify-all-interval-overlaps)
  - [Largest Overlaps of Intervals](#largest-overlaps-of-intervals)
- [Char 10 Prefix Sums](#char-10-prefix-sums)
  - [Sum between range](#sum-between-range)
  - [K-sum Subarrays](#k-sum-subarrays)
  - [Optimization: Hash Map (Similar to Pair Sum - Unsorted, in Hash Maps Chapter)](#optimization-hash-map-similar-to-pair-sum---unsorted-in-hash-maps-chapter)
  - [Product Array without current element](#product-array-without-current-element)
- [Char 11 Trees](#char-11-trees)
  - [DFS](#dfs)
  - [BFS](#bfs)
  - [Invert Binary Tree (Mirror of itself)](#invert-binary-tree-mirror-of-itself)
    - [Recursive](#recursive)
    - [Iteration](#iteration)
  - [Balanced Binary Tree Validation](#balanced-binary-tree-validation)
  - [Rightmost nodes of a binary tree](#rightmost-nodes-of-binary-tree)
  - [Widest Binary Tree Level](#widest-binary-tree-level)
  - [Binary Search Tree Validation](#binary-search-tree-validation)
  - [Lowest Common Ancestor (LCA)](#lowest-common-ancestor-lca)
  - [Build Binary Tree from Preorder and Inorder Traversals](#build-binary-tree-from-preorder-and-inorder-traversals)
  - [Max Sum of Continuous Path in Binary Tree](#max-sum-of-continuous-path-in-binary-tree)
  - [Binary Tree Symmetry](#binary-tree-symmetry)
  - [Binary Tree Columns](#binary-tree-columns)
  - [K-th Smallest Number in Binary Search Tree](#k-th-smallest-number-in-binary-search-tree)
    - [Recursive](#recursive-1)
    - [Iterative](#iterative)
  - [Serialize and Deserialize Binary Tree](#serialize-and-deserialize-binary-tree)
- [Char 12 Tries](#char-12-tries)
  - [Insert and Search Words with Wildcards](#insert-and-search-words-with-wildcards)
  - [Find All Words on a Board](#find-all-words-on-a-board)
- [Char 13 Graphs](#char-13-graphs)
  - [Graph Deep Copy](#graph-deep-copy)
  - [Count Islands](#count-islands)
  - [Matrix Infection](#matrix-infection)
  - [Bipartite Graph Validation](#bipartite-graph-validation)
  - [Longest Increasing Path](#longest-increasing-path)
  - [Shortest Transformation Sequence](#shortest-transformation-sequence)
  - [Optimization - Bidirectional Traversal](#optimization---bidirectional-traversal)
  - [Merging Communities](#merging-communities)
  - [Prerequisites](#prerequisites)
  - [Shortest Path](#shortest-path)
  - [Connect Dots](#connect-dots)
- [Char 14 Backtracking](#char-14-backtracking)
  - [Find All Permutations](#find-all-permutations)
  - [Find All Subsets](#find-all-subsets)
  - [N Queens](#n-queens)
  - [Combinations of a Sum](#combinations-of-a-sum)
  - [Phone Keypad Combinations](#phone-keypad-combinations)
- [Char 15 Dynamic Programming](#char-15-dynamic-programming)
  - [Climbing Stairs](#climbing-stairs)
    - [Top-down](#top-down)
    - [Botom-up](#botom-up)
    - [Optimization - bottom up](#optimization---bottom-up)
  - [Min Coin Combination](#min-coin-combination)
    - [Top Down](#top-down-1)
    - [Bottom up](#bottom-up)
  - [Matrix Pathways](#matrix-pathways)
    - [Optimized](#optimized-1)
  - [Neighborhood Burglary](#neighborhood-burglary)
    - [Optimization](#optimization)
  - [Longest Common Subsequence (LCS)](#longest-common-subsequence-lcs)
    - [Optimization](#optimization-1)
  - [Longest Palindrome in String](#longest-palindrome-in-string)
  - [Max Subarray Sum](#max-subarray-sum)
  - [0/1 Knapsack](#0-1-knapsack)
  - [Largest Square in Matrix](#largest-square-in-matrix)
    - [Optimization](#optimization-2)
- [Char 16 Greedy](#char-16-greedy)
  - [Jump to End](#jump-to-end)
  - [Gas Stations](#gas-stations)
  - [Candies](#candies)
- [Char 17 Sort and Search](#char-17-sort-and-search)
  - [Sort Linked List](#sort-linked-list)
  - [Sort Array](#sort-array)
  - [K-th Largest Integer](#k-th-largest-integer)
    - [Quickselect](#quickselect)
  - [Dutch National Flag](#dutch-national-flag)
- [Char 18 Bit Manipulation](#char-18-bit-manipulation)
  - [Hamming Weights of Integers](#hamming-weights-of-integers)
  - [Lonely Integer](#lonely-integer)
  - [Swap Odd and Even Bits](#swap-odd-and-even-bits)
- [Char 19 Math and Geometry](#char-19-math-and-geometry)
  - [Spiral Traversal](#spiral-traversal)
  - [Reverse 32-bit Integer](#reverse-32-bit-integer)
  - [Max Collinear Points](#max-collinear-points)
  - [Josephus Problem](#josephus-problem)
  - [Triangle Numbers](#triangle-numbers)
- [Templates](#Templates)

<!-- TOC --><a name="char-1-two-pointers"></a>

# Char 1 Two Pointers

<!-- TOC --><a name="pair-sum-sorted"></a>

## Pair Sum - Sorted

```python
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        # if sum smaller, increment left pointer, aiming
        # to increase sum toward the target value
        if sum < target:
            left += 1
        # if sum larger, decrement right pointer, aiming
        # to decrease sum toward the target value
        elif sum > target:
            right -= 1
        # if target pair not found, return its indexes
        else:
            return [left, right]
    return []
```

<!-- TOC --><a name="triplet-sum"></a>

## Triplet Sum

```python
def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sort()
    for i in range(len(nums)):
        # optimization: triplets consisting of only positive numbers
        # will never sum to 0
        if nums[i] > 0:
            break
        # avoid duplicate triplets, skip it if same as previous number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # find all pairs that sum to a target of '-a'
        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
        for pair in pairs:
            triplets.append([nums[i]] + pair)
    return triplets

def pair_sum_sorted_all_pairs(nums: List[int],
                              start: int, target: int) -> List[int]:
    pairs = []
    left, right = start, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            # to avoid duplicate '[b, c]' pairs, skip 'b' if same as previous number
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1
    return pairs
```

<!-- TOC --><a name="palindrome-valid"></a>

## palindrome valid

```python
def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

<!-- TOC --><a name="largest-container"></a>

## largest container

```python
def largest_container(heights: List[int]) -> int:
    max_water = 0
    left, right = 0, len(heights) - 1
    while (left < right):
        # calculate water contained between current pair of lines
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)
        # move pointers inward, always moving pointer at shorter line
        # if both lines have same height, move both pointers inward
        if (heights[left] < heights[right]):
            left += 1
        elif (heights[left] > heights[right]):
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water
```

## Shift Zeros to the End

```python
def shift_zeros_to_the_end(nums: List[int]) -> None:
    # left pointer is used to position non-0 elements
    left = 0
    # iterate through array using right pointer to locate non-0 elements
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            # increment left since it points to position already occupied by non-0 elementr
            left += 1
```

## Next Lexicographical Sequence

```python
def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    # locate pivot, the first character from the right that breaks
    # non-increasing order. Start searching from second-to-last position,
    # since the last character is neither increasing nor decreasing
    pivot = len(letters) - 2
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1
    # if pivot not found, string already in largest permutation. Then, reverse string to obtain smallest permutation
    if pivot == -1:
        return ''.join(reversed(letters))
    # find rightmost successor to the pivot
    rightmost_successor = len(letters) - 1
    while letters[rightmost_successor] <= letters[pivot]:
        rightmost_successor -= 1
    # swap rightmost successor with pivot to increase lexicographical order of suffix
    letters[pivot], letters[rightmost_successor] = (letters[rightmost_successor], letters[pivot])
    # Reverse suffix after pivot to min its permutation
    letters[pivot + 1:] = reversed(letters[pivot + 1:])
    return ''. join(letters)
```

<!-- TOC --><a name="char-2-hash-map"></a>

# Char 2 Hash Map

<!-- TOC --><a name="pair-sum-unsorted"></a>

## Pair Sum Unsorted

```python
def pair_sum_unsorted_two_pass(nums: List[int],
                               target: int) -> List[int]:
    num_map = {}
    # first pass: populate hash map with each number and its index
    for i, num in enumerate(nums):
        num_map[num] = i
    # second pass: check for each number's complement in hash map
    for i, num in enumerate(nums):
        complement = target - sum
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
    return []

def pair_sum_unsorted(nums: List[int],
                      target: int) -> List[int]:
    hashmap = {}
    for i, x in enumerate(nums):
        if target - x in hashmap:
            return [hashmap[target - x], i]
        hashmap[x] = i
    return []
```

<!-- TOC --><a name="verify-sudoku-board"></a>

## Verify Sudoku Board

```python
def verify_sudoku_board(board: List[List[int]]) -> bool:
    # create hash sets for each row, column, subgrid to keep track of
    # numbers previously seen on any given row, column, subgrid
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                continue
            # check if num has been seen in current row, column, subgrid
            if num in row_sets[r]:
                return False
            if num in column_sets[c]:
                return False
            if num in subgrid_sets[r // 3][c // 3]:
                return False
            row_sets[r].add(num)
            column_sets[c].add(num)
            subgrid_sets[r // 3][c // 3].add(num)
    return True
```

<!-- TOC --><a name="zero-stripping"></a>

## Zero stripping

```python
def zero_stripping_hash_sets(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    # pass 1: traverse through matrix to identify rows and columns
    # containing 0s and store their indexes in the hash sets
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    # pass 2: set any cell in matrix to 0 if row index is in zero_rows
    # or its column index is in zero_cols
    for r in range(m):
        for c in range(n):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0
```

## Longest Chain of Consecutive Numbers

```python
def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if not nums:
        return 0
    num_set = set(nums)
    longest_chain = 0
    for num in num_set:
        # if current num is smallest in chain, search for length of chain
        if num - 1 not in num_set:
            current_num = num
            current_chain = 1
            # continue to find next consecutive numbers in the chain
            while (current_num + 1) in num_set:
                current_num += 1
                current_chain += 1
            longest_chain = max(longest_chain, current_chain)
    return longest_chain
```

## Geometric Sequence Triplets

```python
def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    # use defaultdict to ensure default value of 0 is returned when accessing a key not exist in hash map
    # this effectively sets default frequency of all elements to 0
    left_map = defaultdict(int)
    right_map = defaultdict(int)
    count = 0
    # populate right_map with frequency of each element in array
    for x in nums:
        right_map[x] += 1
    # search for geometric triplets that have x as center
    for x in nums:
        # decrement the frequency of x in right_map since x is now being processed and is no longer to the right
        right_map[x] -= 1
        if x % r == 0:
            count += left_map[x // r] * right_map[x ** r]
        # increment frequency of x in left_map since it'll be part of the left side of array once we iterate to the next value of x
        left_map[x] += 1
    return count
```

<!-- TOC --><a name="char-3-linked-list"></a>

# Char 3 Linked List

```python
class ListNode:
    def __init__(self, val: int, next: ListNode):
        self.val = val
        self.next = next

def linked_list_reversal(head: ListNode) -> ListNode:
    curr_node, prev_node = head, None
    # reverse direction of each node's pointer until curr_node is null
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    # prev_node will be pointing at the head of the reversed linked list
    return prev_node

def linked_list_reversal_recursive(head: ListNode) -> ListNode:
    # base cases
    if (not head) or (not head.next):
        return head
    # recursively reverse sublist starting from the next node
    new_head = linked_list_reversal_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

<!-- TOC --><a name="remove-k-th-last-node"></a>

## remove k-th last node

```python
def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    # dummy node to ensure a node before head in case we need to remove head
    dummy = ListNode(-1)
    dummy.next = head
    trailer = leader = dummy
    # advance leader k steps ahead
    for _ in range(k):
        leader = leader.next
        # if k > length of linked list, no need to remove node
        if not leader:
            return head
    # move leader to the end of linked list, keeping trailer k nodes behind
    while leader.next:
        leader = leader.next
        trailer = trailer.next
    # remove kth node from the end
    trailer.next = trailer.next.next
    return dummy.next
```

<!-- TOC --><a name="linked-list-intersection"></a>

## linked list intersection

```python
def linked_list_intersection(head_A: ListNode,
                             head_B: ListNode) -> ListNode:
    ptr_A, ptr_B = head_A, head_B
    # traverse through list A with ptr_A and list B with ptr_B until meeting
    while ptr_A != ptr_B:
        # traverse list A -> list B by first traversing ptr_A and then,
        # upon reaching the end of list A, continue traversal from head of list B
        ptr_A = ptr_A.next if ptr_A else head_B
        # simultaneously, traverse list B -> list A
        ptr_B = ptr_B.next if ptr_B else head_A
    # ptr_A and ptr_B either point to intersection node or both are null if lists don't intersect
    # return either pointer
    return ptr_A
```

<!-- TOC --><a name="lru-cache"></a>

## LRU cache

```python
class DoublyLinkedListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = self.prev = None
    def add_to_tail(self, node: DoublyLinkedListNode) -> None:
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node
    def remove_node(self, node: DoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # hash map that maps keys to nodes
        self.hashmap = {}
        # initialize head and tail dummy nodes and connect to each other
        # to establish a basic 2-node doubly linked list
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        # to make the key most recently used, remove its node and
        # readd it to the tail of linked list
        self.remove_node(self.hashmap[key])
        self.add_to_tail(self.hashmap[key])
        return self.hashmap[key].val
    def put(self, key: int, value: int) -> None:
        # if node with this key exists, remove from linked list
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])
        node = DoublyLinkedListNode(key, value)
        self.hashmap[key] = node
        # remove least recently used node from cache if adding
        # this new node will result in overflow
        if len(self.hashmap) > self.capacity:
            del self.hashmap[self.head.next.key]
            self.remove_node(self.head.next)
        self.add_to_tail(node)
```

## Palindromic Linked List

```python
def palindromic_linked_list(head: ListNode) -> bool:
    # find middle of the linked list and reverse second half of the linked list starting at midpoint
    mid = find_middle(head)
    second_head = reverse_list(mid)
    # compare first half and reversed second half of the linked list
    ptr1, ptr2 = head, second_head
    res = True
    while ptr2:
        if ptr1.val != ptr2.val:
            res = False
        ptr1, ptr2 = ptr1.next, ptr2.next
    return res

def reverse_list(head: ListNode) -> ListNode:
    prevNode, currNode = None, head
    while currNode:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    return prevNode

def find_middle(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

## Flatten a Multi-Level Linked List

```python
class MultiLevelListNode:
    def __init__(self, val, next, child):
        self.val = val
        self.next = next
        self.child = child

def flatten_multi_level_list(head: MultiLevelListNode) -> MultiLevelListNode:
    if not head:
        return None
    tail = head
    # find tail of linked list at first level
    while tail.next:
        tail = tail.next
    curr = head
    # process each node at current level. If node has child linked list, append it to the tail and update tail to the end of extended linked list
    # continue until all nodes at the current level are processed
    while curr:
        if curr.child:
            tail.next = curr.child
            # diconnect child linked list from current node
            curr.child = None
            while tail.next:
                tail = tail.next
        curr = curr.next
    return head
```

<!-- TOC --><a name="char-4-fast-slow-pointers"></a>

# Char 4 Fast Slow Pointers

<!-- TOC --><a name="linked-list-loop"></a>

## Linked List Loop

```python
def linked_list_loop_naive(head: ListNode) -> bool:
    visited = set()
    curr = head
    while curr:
        # cycle detected if the current node has been visited
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False

def linked_list_loop(head: ListNode) -> bool:
    slow = fast = head
    # check both fast and fast.next to avoid null pointer
    # exceptions when fast.next and fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
```

<!-- TOC --><a name="linked-list-midpoint"></a>

## Linked List Midpoint

```python
def linked_list_midpoint(head: ListNode) -> ListNode:
    slow = fast = head
    # when fast pointer reaches the end, slow reaches midpoint
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

<!-- TOC --><a name="happy-number"></a>

## Happy Number

```python
def happy_number(n: int) -> bool:
    slow = fast = n
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))
        if fast == 1:
            return True
        # if fast and slow pointers meet, a cycle is detected
        # Hence, n is not happy number
        elif fast == slow:
            return True

def get_next_num(x: int) -> int:
    next_num = 0
    while x > 0:
        # extract last digit of x
        digit = x % 10
        x //= 10
        next_num += digit ** 2
    return next_num
```

## Happy Number

```python
def happy_number(n: int) -> bool:
    slow = fast = n
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))
        if fast == 1:
            return True
        # if fast and slow pointers meet, a cycle is detected
        # Hence, n is not happy number
        elif fast == slow:
            return True

def get_next_num(x: int) -> int:
    next_num = 0
    while x > 0:
        # extract last digit of x
        digit = x % 10
        x //= 10
        next_num += digit ** 2
    return next_num
```

<!-- TOC --><a name="char-5-sliding-windows"></a>

# Char 5 Sliding Windows

<!-- TOC --><a name="substring-anagrams"></a>

## Substring Anagrams

```python
def substring_anagrams(s: str, t: str) -> int:
    len_s, len_t = len(s), len(t)
    if len_t > len_s:
        return 0
    count = 0
    expected_freqs, window_freqs = [0] * 26, [0] * 26
    # populate expected_freqs with the characters in string t
    for c in t:
        expected_freqs[ord(c) - ord('a')] += 1
    left = right = 0
    while right < len_s:
        # add character at right pointer to window_freqs before sliding window
        window_freqs[ord(s[right]) - ord('a')] += 1
        # if window has reached expected fixed length, advance left pointer
        # as well as right pointer to slide window
        if right - left + 1 == len_t:
            if window_freqs == expected_freqs:
                count += 1
            # remove character at left pointer from window_freqs before advancing left pointer
            window_freqs[ord(s[left]) - ord('a')] -= 1
            left += 1
        right += 1
    return count
```

<!-- TOC --><a name="longest-substring-with-unique-characters"></a>

## Longest substring with unique characters

```python
def longest_substring_with_unique_chars(s: str) -> int:
    max_len = 0
    hash_set = set()
    left = right = 0
    while right < len(s):
        # if encounter duplicate character in window, shrink window
        # until it's no longer a duplicate
        while s[right] in hash_set:
            hash_set.remove(s[left])
            left += 1
        # once no more duplicates in window, update max_len
        # if current window is larger
        max_len = max(max_len, right - left + 1)
        hash_set.add(s[right])
        right += 1
    return max_len
```

<!-- TOC --><a name="optimized"></a>

## optimized

```python
def longest_substring_with_unique_chars(s: str) -> int:
    max_len = 0
    prev_indexes = {}
    left = right = 0
    while right < len(s):
        # if previous index of current character is present in
        # current window, it's duplicate character in the window
        if (s[right] in prev_indexes and
            prev_indexes[s[right]] >= left):
            # shrink window to exclude previous occurence of character
            left = prev_indexes[s[right]] + 1
        # update max_len if current window is larger
        max_len = max(max_len, right - left + 1)
        prev_indexes[s[right]] = right
        # expand window
        right += 1
    return max_len
```

<!-- TOC --><a name="longest-uniform-substring-after-replacement"></a>

## Longest Uniform substring after replacement

```python
def longest_uniform_substring_after_replacement(s: str, k: int) -> int:
    freqs = {}
    highest_freq = max_len = 0
    left = right = 0
    while right < len(s):
        # update freq of character at right pointer and highest freq for current window
        freqs[s[right]] = freqs.get(s[right], 0) + 1
        highest_freq = max(highest_freq, freqs[s[right]])
        # calculate replacements needed for current window
        num_chars_to_replace = (right - left + 1) - highest_freq
        # slide window if number of replacements needed exceeds k
        # right pointer always gets advenced, so we just need to advance left
        if num_chars_to_replace > k:
            # remove character at left pointer from hash map before advancing left pointer
            freqs[s[left]] -= 1
            left += 1
        # since length of current window increases or stays the same,
        # assign length of current window to max_len
        max_len = right - left + 1
        # expand window
        right += 1
    return max_len
```

<!-- TOC --><a name="char-6-binary-search"></a>

# Char 6 Binary Search

<!-- TOC --><a name="find-insertion-index"></a>

## Find Insertion Index

```python
def find_the_insertion_index(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        # if midpoint >= target, lower bound  <=  midpoint
        if nums[mid] >= target:
            right = mid
        # midpoint < target, lower bounnd > midpoint
        else:
            left = mid + 1
    return left
```

<!-- TOC --><a name="first-and-last-occurrence-of-number"></a>

## First and Last Occurrence of Number

```python
def first_and_last_occurrences_of_a_number(nums: List[int],
                                           target: int) -> List[int]:
    lower_bound = lower_bound_binary_search(nums, target)
    upper_bound = upper_bound_binary_search(nums, target)
    return [lower_bound, upper_bound]

def lower_bound_binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if nums and nums[left] == target else -1

def upper_bound_binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        # upper bound binary search, bias the midpoint to the right
        mid = (left + right) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            left = mid
    return right if nums and nums[right] == target else -1
```

<!-- TOC --><a name="cutting-wood"></a>

## Cutting Wood

```python
def cutting_wood(heights: List[int], k: int) -> int:
    left, right = 0, max(heights)
    while left < right:
        # bias the midpoint to the right during upper bound binary search
        mid = (left + right) // 2 + 1
        if cuts_enough_wood(mid, k, heights):
            left = mid
        else:
            right = mid - 1
    return right
```

<!-- TOC --><a name="determine-if-current-value-of-h-cuts-at-least-k-meters-of-wood"></a>

# Determine if current value of H cuts at least k meters of wood

```python
def cuts_enough_wood(H: int, k: int, heights: List[int]) -> bool:
    wood_collected = 0
    for height in heights:
        if height > H:
            wood_collected += (height - H)
    return wood_collected >= k
```

<!-- TOC --><a name="find-target-in-rotated-sorted-array"></a>

## Find target in rotated sorted array

```python
def find_the_largest_in_a_rotated_sorted_array(nums: List[int],
                                               target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # if left subarray [left: mid] is sorted, check if target falls in this range
        # if yes, search left subarray, if no, search right
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # if right subarray [mid: right] is sorted, check if target falls in
        # if yes, search right, if no, search left
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    # if target found, return index. else, return -1
    return left if nums and nums[left] == target else -1
```

## Find Median From Two Sorted Arrays

```python
def find_the_median_from_two_sorted_arrays(nums1: List[int],
                                           nums2: List[int]) -> float:
    # optimization: ensure nums1 is smaller array
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    half_total_len = (m + n) // 2
    left, right = 0, m - 1
    # median exists in non-empty array, so continue binary search until it's found
    while True:
        L1_index = (left + right) // 2
        L2_index = half_total_len - (L1_index + 1) - 1
        # set to -infinity or +infinity if out of bounds
        L1 = float('-inf') if L1_index < 0 else nums1[L1_index]
        R1 = float('inf') if L1_index >= m - 1 else nums1[L1_index + 1]
        L2 = float('-inf') if L2_index < 0 else nums2[L2_index]
        R2 = float('inf') if L2_index >= n - 1 else nums2[L2_index + 1]
        # if L1 > R2, then L1 is too far to the right. narrow search space toward left
        if L1 > R2:
            right = L1_index - 1
        # if L2 > R1, then L1 is too far to the left. narrow search space toward right
        elif L2 > R1:
            left = L1_index + 1
        # if both L1, L2 <= R1, R2, found the correct slice
        else:
            if (m + n) % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2.0
            else:
                return min(R1, R2)
```

## Matrix Search

```python
def matrix_search(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    # binary search to find target
    while left <= right:
        mid = (left + right) // 2
        r, c = mid // n, mid % n
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
```

## Local Maxima in Array

```python
def local_maxima_in_array(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
```

## Weighted Random Selection

```python
class WeightedRandomSelection:
    def __init__(self, weights: List[int]):
        self.prefix_sums = [weights[0]]
        for i in range(1, len(weights)):
            self.prefix_sums.append(self.prefix_sums[-1] + weights[i])

    def select(self) -> int:
        # pick random target between 1 and largest possible endpoint
        target = random.randint(1, self.prefix_sums[-1])
        left, right = 0, len(self.prefix_sums) - 1
        # perform lower_bound binary search to find which endpoint (prefix sum value) corresponds to the target
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
```

<!-- TOC --><a name="char-7-stack"></a>

# Char 7 Stack

<!-- TOC --><a name="valid-parenthesis-expression"></a>

## Valid Parenthesis Expression

```python
def valid_parenthesis_expression(s: str) -> bool:
    parentheses_map = {'(':')', '{':'}', '[':']'}
    stack = []
    for c in s:
        # if current character is an opening parenthesis, push it into stack
        if c in parentheses_map:
            stack.append(c)
        # if current character is closing parenthesis, check if it closes the opening parenthesis at top of stack
        else:
            if stack and parentheses_map[stack[-1]] == c:
                stack.pop()
            else:
                return False
    # if stack empty, all opening parentheses were closed
    return not stack
```

<!-- TOC --><a name="next-largest-number-to-the-right"></a>

## Next Largest Number to the Right

```python
def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    stack = []
    # Find next largest number of each element, starting with the rightmost element
    for i in range(len(nums) - 1, -1, -1):
        # pop values from top of stack until current value's next largest number is at the top
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        # record current value's next largest number, which is at top of stack
        # if stack empty, record -1
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res
```

<!-- TOC --><a name="evaluate-expression"></a>

## Evaluate Expression

```python
def evaluate_expression(s: str) -> int:
    stack = []
    curr_num, sign, res = 0, 1, 0
    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        # if current character is operator, add curr_num to result after multiplying it by its sign
        elif c == '+' or c == '-':
            res += curr_num * sign
            # update sign and reset curr_num
            sign = -1 if c == '-' else 1
            curr_num = 0
        # if current charater is opening parenthesis, a new nested expression starts
        elif c == '(':
            # save current res and sign values by pushing onto stack
            # then reset values to start calculating
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        # if current character is closing parenthesis, a nested expression ends
        elif c == ')':
            res += sign * curr_num
            # apply sign of current nested expression's result before adding result to the result of outer expression
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0
    # finalize result of overall expression
    return res + curr_num * sign
```

## Repeated Removal of Adjacent Duplicates

```python
def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    stack = []
    for c in s:
        # if current character is same as top character on stack,
        # a pair of adjacent duplicates has been formed. So, pop the top from stack
        if stack and c == stack[-1]:
            stack.pop()
        # other wise, push current character onto stack
        else:
            stack.append(c)
    # return remaining characters as a string
    return ''.join(stack)
```

## Implement Queue Using Stacks

```python
class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, x: int) -> None:
        self.enqueue_stack.append(x)

    def transfer_enqueue_to_dequeue(self) -> None:
        # if dequeue stack is empty, push all elements from enqueue stack onto dequeue stack
        # this ensures top of the dequeue stack contains least recently added value
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

    def dequeue(self) -> int:
        self.transfer_enqueue_to_dequeue()
        # pop and return value at top of dequeue stack
        return self.dequeue_stack.pop() if self.dequeue_stack else None

    def peek(self) -> int:
        self.transfer_enqueue_to_dequeue()
        return self.dequeue_stack[-1] if self.dequeue_stack else None
```

## Max of Sliding Window

```python
def max_of_sliding_window(nums: List[int], k: int) -> List[int]:
    res = []
    dq = deque()
    left = right = 0
    while right < len(nums):
        # ensure values of deque maintain monotonic decreasing order by removing candidates <= current candidate
        while dq and dq[-1][0] <= nums[right]:
            dq.pop()
        # add current candidate
        dq.append((nums[right], right))
        # if window length = k, record max of the window
        if right - left + 1 == k:
            # remove values whose indexes occur outside window
            if dq and dq[0][1] < left:
                dq.popleft()
            # max value of window is leftmost value in deque
            res.append(dq[0][0])
            # slide window by advancing both left and right. right pointer always gets advanced so just need to advance left
            left += 1
        right += 1
    return res
```

<!-- TOC --><a name="char-8-heaps"></a>

# Char 8 Heaps

<!-- TOC --><a name="k-most-frequent-strings"></a>

## K most frequent strings

<!-- TOC --><a name="max-heap"></a>

## Max Heap

```python
class Pair:
    def __init__(self, str, freq):
        self.str = str
        self.freq = freq

    # define custom comparator
    def __lt__(self, other):
        # prioritize lexicographical order for strings with equal freq
        if self.freq == other.freq:
            return self.str < other.str
        # otherwise, prioritize strings with higher freq
        return self.freq > other.freq

def k_most_frequent_strings_max_heap(strs: List[str],
                                     k: int) -> List[str]:
    # use Counter to create hash map that counts frequency of each string
    freqs = Counter(strs)
    # create max heap by preforming heapify on all string-frequency pairs
    max_heap = [Pair(str, freq) for str, freq in freqs.items()]
    heapq.heapify(max_heap)
    # pop most frequent string off the heap k tiems and return k most frequent strings
    return [heapq.heappop(max_heap).str for _ in range(k)]
```

<!-- TOC --><a name="min-heap"></a>

## Min Heap

```python
class Pair:
    def __init__(self, str, freq):
        self.str = str
        self.freq = freq
    # min-heap comparator, use same comparator as the one used in max-heap,
    # but reversing inequality signs to invert priority
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str > other.str
        return self.freq < other.freq

def k_most_frequent_strings_min_heap(strs: List[str],
                                     k: int) -> List[str]:
    freqs = Counter(strs)
    min_heap = []
    for str, freq in freqs.items():
        heapq.heappush(min_heap, Pair(str, freq))
        # if heap size > k, pop lowest freq string to ensure heap only contains the k most freq words so far
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    # return k most frequent strings by popping the remaining k strings from the heap
    # since we use min-heap, we reverse result after popping elements to ensure most frequent strings are listed first
    res = [heapq.heappop(min_heap).str for _ in range(k)]
    res.reverse()
    return res
```

<!-- TOC --><a name="combine-sorted-linked-lists"></a>

## Combine Sorted linked lists

```python
def combine_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    # define custom comparator for ListNode, enabling min-heap to prioritize nodes with smaller values
    ListNode.__lt__ = lambda self, other: self.val < other.val
    heap = []
    # push head of each linked list into heap
    for head in lists:
        if head:
            heapq.heappush(heap, head)
    # set dummy node to point to head of output linked list
    dummy = ListNode(-1)
    # create pointer to iterate through combined linked list as we add nodes to it
    curr = dummy
    while heap:
        # pop node with smallest value from the heap and add it to output linked list
        smallest_node = heapq.heappop(heap)
        curr.next = smallest_node
        curr = curr.next
        # push popped node's subsequent node to the heap
        if smallest_node.next:
            heapq.heappush(heap, smallest_node.next)
    return dummy.next
```

<!-- TOC --><a name="median-of-integer-stream"></a>

## Median of Integer Stream

```python
class MedianOfAnIntegerStream:
    def __init__(self):
        self.left_half = []
        self.right_half = []
    def add(self, num: int) -> None:
        # if num <= max of left_half, it belongs to the left half
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)
            # rebalance heaps if size of left_half > size of right_half + 1
            if len(self.left_half) > len(self.right_half) + 1:
                heapq.heappush(self.right_half,
                               -heapq.heappop(self.left_half))
        # othersie, it belongs to the right half
        else:
            heapq.heappush(self.right_half, num)
            # rebalance heaps if right_half > left_half
            if len(self.left_half) < len(self.right_half):
                heapq.heappush(self.left_half,
                               -heapq.heappop(self.right_half))

    def get_median(self) -> float:
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2.0
        return -self.left_half[0]
```

## Sort K-Sorted Array

```python
def sort_a_k_sorted_array(nums: List[int], k: int) -> List[int]:
    # populate min-heap with first k + 1 values in nums
    min_heap = nums[:k+1]
    heapq.heapify(min_heap)
    # replace elements in array with min from the heap at each iteration
    insert_index = 0
    for i in range(k + 1, len(nums)):
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
        heapq.heappush(min_heap, nums[i])
    # pop remaining elements from heap to finish sorting array
    while min_heap:
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
    return nums
```

<!-- TOC --><a name="char-9-interval"></a>

# Char 9 Interval

<!-- TOC --><a name="merge-overlapping-intervals"></a>

## Merge Overlapping Intervals

```python
def merge_overlappinng_intervals(
        intervals: List[Interval]
) -> List[Interval]:
    intervals.sort(key=lambda x: x.start)
    merged = [intervals[0]]
    for B in intervals[1:]:
        A = merged[-1]
        # if A, B don't overlap, add B to merged list
        if A.end < B.start:
            merged.append(B)
        # if overlap, merge A with B
        else:
            merged[-1] = Interval(A.start, max(A.end, B.end))
    return merged

```

<!-- TOC --><a name="identify-all-interval-overlaps"></a>

## Identify All Interval Overlaps

```python
def identify_all_interval_overlaps(
        intervals1: List[Interval], intervals2: List[Interval]
) -> List[Interval]:
    overlaps = []
    i = j = 0
    while i < len(intervals1) and j < len(intervals2):
        # set A to interval that starts first and B to the other interval
        if intervals1[i].start <= intervals2[j].start:
            A, B = intervals1[i], intervals2[j]
        else:
            A, B = intervals2[j], intervals1[i]
        # if overlap, add overlap
        if A.end >= B.start:
            overlaps.append(Interval(B.start, min(A.end, B.end)))
        # advance pointer with interval that ends first
        if intervals1[i].end < intervals2[i].end:
            i += 1
        else:
            j += 1
    return overlaps
```

<!-- TOC --><a name="largest-overlaps-of-intervals"></a>

## Largest Overlaps of Intervals

```python
def largest_overlap_of_intervals(intervals: List[Interval]) -> int:
    points = []
    for interval in intervals:
        points.append((interval.start, 'S'))
        points.append((interval.end, 'E'))
    # sort in chronological order. If multiple points occur at the same time,
    # ensure end points are prioritized before start points.
    points.sort(key=lambda x: (x[0], x[1]))
    active_intervals = 0
    max_overlaps = 0
    for time, point_type in points:
        if point_type == 'S':
            active_intervals += 1
        else:
            active_intervals -= 1
        max_overlaps = max(max_overlaps, active_intervals)
    return max_overlaps
```

<!-- TOC --><a name="char-10-prefix-sums"></a>

# Char 10 Prefix Sums

```python
def prefix_sums(sums):
    # start by adding the first number to the prefix sum array
    prefix_sum = [nums[0]]
    # for all remaining indexes, add them in
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[-1] + nums[i])
```

<!-- TOC --><a name="sum-between-range"></a>

## Sum between range

```python
class SumBetweenRange:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sum_range(self, i: int, j: int) -> int:
        if i == 0:
            return self.prefix_sum[j]
        return self.prefix_sum[j] - self.prefix_sum[i - 1]
```

<!-- TOC --><a name="k-sum-subarrays"></a>

## K-sum Subarrays

```python
def k_sum_subarrays(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    # populate prefix sum array, setting first element = 0
    prefix_sum = [0]
    for i in range(0, n):
        prefix_sum.append(prefix_sum[-1] + nums[i])
    # loop through all valid pairs of prefix sum values to find subarrays that sum to k
    for j in range(1, n + 1):
        for i in range(1, j + 1):
            if prefix_sum[j] - prefix_sum[i - 1] == k:
                count += 1
    return count
```

<!-- TOC --><a name="optimization-hash-map-similar-to-pair-sum-unsorted-in-hash-maps-chapter"></a>

## Optimization: Hash Map (Similar to Pair Sum - Unsorted, in Hash Maps Chapter)

```python
def k_sum_subarrays_optimized(nums: List[int], k: int) -> int:
    count = 0
    # initialize map with 0 to handle subarrays that sum to k from start of array
    prefix_sum_map = {0: 1}
    curr_prefix_sum = 0
    for num in nums:
        # update running prefix sum by adding current number
        curr_prefix_sum += num
        # if subarry with sum k exists, increment count by the number of times it's found
        if curr_prefix_sum - k in prefix_sum_map:
            count += prefix_sum_map[curr_prefix_sum - k]
        # update freq of curr_prefix_sum in hash map
        freq = prefix_sum_map.get(curr_prefix_sum, 0)
        prefix_sum_map[curr_prefix_sum] = freq + 1
    return count
```

<!-- TOC --><a name="product-array-without-current-element"></a>

## Product Array without current element

```python
def product_array_without_current_element(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    # multiply output with running right product, from right to left
    right_product = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]
    return res
```

<!-- TOC --><a name="char-11-trees"></a>

# Char 11 Trees

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

<!-- TOC --><a name="dfs"></a>

## DFS

```python
def dfs(node: TreeNode):
    if node is None:
        return
    process(node)
    dfs(node.left)
    dfs(node.right)
```

<!-- TOC --><a name="bfs"></a>

## BFS

```python
def bfs(root: TreeNode):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        process(node)
        if node.left:
            # add left child to queue
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

<!-- TOC --><a name="invert-binary-tree-mirror-of-itself"></a>

## Invert Binary Tree (Mirror of itself)

<!-- TOC --><a name="recursive"></a>

### Recursive

```python
def invert_binary_tree_recursive(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_binary_tree_recursive(root.left)
    invert_binary_tree_recursive(root.right)
    return root
```

<!-- TOC --><a name="iteration"></a>

### Iteration

```python
def invert_binary_tree_iterative(root: TreeNode) -> TreeNode:
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        # swap left and right subtrees of current node
        node.left, node.right = node.right, node.left
        # push left and right subtrees onto stack
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root
```

<!-- TOC --><a name="balanced-binary-tree-validation"></a>

## Balanced Binary Tree Validation

```python
def balanced_binary_tree_validation(root: TreeNode) -> bool:
    return get_height_imbalance(root) != -1
def get_height_imbalance(node: TreeNode) -> int:
    # base case: if node null, height = 0
    if not node:
        return 0
    # recursively get height of left and right subtrees.
    # If either subtree is imbalanced, propagate -1 up the tree
    left_height = get_height_imbalance(node.left)
    right_height = get_height_imbalance(node.right)
    if left_height == -1 or right_height == -1:
        return -1
    # if current node's subtree is imbalanced
    if abs(left_height - right_height) > 1:
        return -1
    # return height of current subtree
    return 1 + max(left_height, right_height)
```

<!-- TOC --><a name="rightmost-nodes-of-binary-tree"></a>

## Rightmost nodes of binary tree

```python
def rightmost_nodes_of_a_binary_tree(root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        # add all non-null child nodes of current level to the queue
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # record this level's last node to result array
            if i == level_size - 1:
                res.append(node.val)
    return res
```

<!-- TOC --><a name="widest-binary-tree-level"></a>

## Widest Binary Tree Level

```python
def widest_binary_tree_level(root: TreeNode) -> int:
    if not root:
        return 0
    max_width = 0
    queue = deque([(root, 0)]) # stores (node, index) pairs
    while queue:
        level_size = len(queue)
        # set leftmost_index to index of the first node in this level
        # start rightmost_index at the same point as leftmost_index and udpate it as we traverse the level
        # eventually positioning it at the last node
        leftmost_index = queue[0][1]
        rightmost_index = leftmost_index
        # process all nodes at current level
        for _ in range(level_size):
            node, i = queue.popleft()
            if node.left:
                queue.append((node.left, 2 * i + 1))
            if node.right:
                queue.append((node.right, 2 * i + 2))
            rightmost_index = i
        max_width = max(max_width, rightmost_index - leftmost_index + 1)
    return max_width
```

<!-- TOC --><a name="binary-search-tree-validation"></a>

## Binary Search Tree Validation

```python
def binary_search_tree_validation(root: TreeNode) -> bool:
    # start validation at root node, can contain value, so set initial lower and upper bound to infinity
    return is_within_bounds(root, float('-inf'), float('inf'))

def is_within_bounds(node: TreeNode,
                     lower_bound: int, upper_bound: int) -> bool:
    # base case, if node null, it satisfies BST
    if not node:
        return True
    # if current node's value is not within bounds, it's not valid
    if not lower_bound < node.val < upper_bound:
        return False
    # if left subtree isn't BST, it's not valid
    if not is_within_bounds(node.left, lower_bound, node.val):
        return False
    # otherwise, true
    return is_within_bounds(node.right, node.val, upper_bound)
```

<!-- TOC --><a name="lowest-common-ancestor-lca"></a>

## Lowest Common Ancestor (LCA)

```python
def lowerst_common_ancestor(root: TreeNode,
                            p: TreeNode, q: TreeNode) -> TreeNode:
    dfs(root, p, q)
    return lca

def dfs(node: TreeNode, p: TreeNode, q: TreeNode) -> bool:
    global lca
    # base case: a null node is neither p nor q
    if not node:
        return False
    node_is_p_or_q = node == p or node == q
    ## recursively determine if left and right subtrees contain p or q
    left_contains_p_or_q = dfs(node.left, p, q)
    right_contains_p_or_q = dfs(node.right, p, q)
    # if 2 of above 3 variables are true, current node is LCA
    if (node_is_p_or_q + left_contains_p_or_q + right_contains_p_or_q == 2):
        lca = node
    # return true if current subtree contains p or q
    return (node_is_p_or_q or left_contains_p_or_q or right_contains_p_or_q)
```

<!-- TOC --><a name="build-binary-tree-from-preorder-and-inorder-traversals"></a>

## Build Binary Tree from Preorder and Inorder Traversals

```python
preorder_index = 0
inorder_indexes_map = {}

def build_binary_trees(preorder: List[int], inorder: List[int]) -> TreeNode:
    global inorder_indexes_map
    # populate hash map with inorder values and their indexes
    for i, val in enumerate(inorder):
        inorder_indexes_map[val] = i
    # build tree and return root
    return build_subtree(0, len(inorder) - 1, preorder, inorder)

def build_subtree(left: int, right: int, preorder: List[int], inorder: List[int]) -> TreeNode:
    global preorder_index, inorder_indexes_map
    # base case: if no elements in this range return None
    if left > right:
        return None
    val = preorder[preorder_index]
    # set inorder_index to the index of same value pointed by preorder_index
    inorder_index = inorder_indexes_map[val]
    node = TreeNode(val)
    # advance preorder_index so it points to the value of next node to be created
    preorder_index += 1
    # build left and right subtrees and connect to current node
    node.left = build_subtree(left, inorder_index - 1, preorder, inorder)
    node.right = build_binary_trees(inorder_index + 1, right, preorder, inorder)
    return node
```

<!-- TOC --><a name="max-sum-of-continuous-path-in-binary-tree"></a>

## Max Sum of Continuous Path in Binary Tree

```python
max_sum = float('-inf')

def max_path_sum(root: TreeNode) -> int:
    global max_sum
    max_path_sum_helper(root)
    return max_sum

def max_path_sum_helper(node: TreeNode) -> int:
    global max_sum
    # base case: null nodes have no path sum
    if not node:
        return 0
    # collect max gain we can attain from left and right subtrees, set to 0 if negative
    left_sum = max(max_path_sum_helper(node.left), 0)
    right_sum = max(max_path_sum_helper(node.right), 0)
    # update overall max path sum if current path sum is larger
    max_sum = max(max_sum, node.val + left_sum + right_sum)
    # return max sum of a single, continuous path with current node as endpoint
    return node.val + max(left_sum, right_sum)
```

## Binary Tree Symmetry

```python
def binary_tree_symmetry(root: TreeNode) -> bool:
    if not root:
        return True
    return dfs(root.left, root.right)

def dfs(node1: TreeNode, node2: TreeNode) -> bool:
    # base case: if both nodes null, they're symmetric
    if not node1 and not node2:
        return True
    # if one node is null and other not, they're not symmetric
    if not node1 or node2:
        return False
    # if values of current node don't match, not symmetric
    if node1.val != node2.val:
        return False
    # compare node1's left subtree with node2's right subtree. If not symmetric, then not symmetric
    if not dfs(node1.left, node2.right):
        return False
    # compare node1's right subtree with node2's left subtree
    return dfs(node1.right, node2.left)
```

## Binary Tree Columns

```python
def binary_tree_columns(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    column_map = defaultdict(list)
    leftmost_column = rightmost_column = 0
    queue = deque([(root, 0)])
    while queue:
        node, column = queue.popleft()
        if node:
            # add current node's value to corresponding list in hash map
            column_map[column].append(node.val)
            leftmost_column = min(leftmost_column, column)
            rightmost_column = max(rightmost_column, column)
            # add current node's children to queue with respective column ids
            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))
    # construct output list by collecting values from each column in hash map in correct order
    return [column_map[i] for i in range(leftmost_column, rightmost_column + 1)]
```

## K-th Smallest Number in Binary Search Tree

### Recursive

```python
def kth_smallest_number_in_BST_recursive(root: TreeNode, k: int) -> int:
    sorted_list = inorder(root)
    return sorted_list[k - 1]

# inorder traversal function to attain sorted list of nodes from BST
def inorder(node: TreeNode) -> List[int]:
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)
```

### Iterative

```python
def kth_smallest_number_in_BST_iterative(root: TreeNode, k: int) -> int:
    stack = []
    node = root
    while stack or node:
        # move to leftmost node and add nodes to stack as we go, so they can be processed in future iterations
        while node:
            stack.append(node)
            node = node.left
        # pop top node from stack to process it and decrement k
        node = stack.pop()
        k -= 1
        # if have processed k nodes, return value of kth smallest node
        if k == 0:
            return node.val
        # move to right subtree
        node = node.right
```

## Serialize and Deserialize Binary Tree

```python
def build_tree(values: List[str]) -> TreeNode:
    val = next(values)
    # base case: # indicates a null node
    if val == '#':
        return None
    # use preorder traversal to create current node first, then left and right subtrees
    node = TreeNode(int(val))
    node.left = build_tree(values)
    node.right = build_tree(values)
    return node

def serialize(root: TreeNode) -> str:
    # perform preorder traversal to add node values to list, then convert list to string
    serialized_list = []
    preorder_serialize(root, serialized_list)
    # convert list to string and separate each value using comma delimeter
    return ','.join(serialized_list)

# helper function to perform serialization through preorder traversal
def preorder_serialize(node, serialized_list) -> None:
    # base case: mark null nodes as #
    if node is None:
        serialized_list.append('#')
        return
    # preorder traversal processes the current node first, then left and right children
    serialized_list.append(str(node.val))
    preorder_serialize(node.left, serialized_list)
    preorder_serialize(node.right, serialized_list)

def deserialize(data: str) -> TreeNode:
    # obtain node values by splitting string using comma delimiter
    node_values = iter(data.split(','))
    return build_tree(node_values)

# helper function to contruct tree using preorder traversal
def build_tree(values: List[str]) -> TreeNode:
    val = next(values)
    # base case: # indicates a null node
    if val == '#':
        return None
    # use preorder traversal processes the current node first, then left and right children
    node = TreeNode(int(val))
    node.left = build_tree(values)
    node.right = build_tree(values)
    return node
```

<!-- TOC --><a name="char-12-tries"></a>

# Char 12 Tries

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            # for each character, if not a child, create new TrieNode for it
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # mark the last node as end of a word
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            # for each character in the word, if not child of current node, word doesn't exist
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word
    def has_prefix(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
```

<!-- TOC --><a name="insert-and-search-words-with-wildcards"></a>

## Insert and Search Words with Wildcards

```python
class InsertAndSearchWordsWithWildcards:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        # start searching from root of trie
        return self.search_helper(0, word, self.root)
    def search_helper(self, word_index: int, word: str, node: TrieNode) -> bool:
        for i in range(word_index, len(word)):
            c = word[i]
            # if wildcard character is encountered, recursively search for the rest of the word from each child node
            if c == '.':
                for child in node.children.values():
                    # if match found, return true
                    if self.search_helper(i + 1, word, child):
                        return True
                return False
            elif c in node.children:
                node = node.children[c]
            else:
                return False
        # after processing the last character, return true if reaching end of the word
        return node.is_word
```

<!-- TOC --><a name="find-all-words-on-a-board"></a>

## Find All Words on a Board

```python
def dfs(r, c, board, node):
    temp = board[r][c]
    board[r][c] = '#' # mark as visited
    for next_r, next_c in adjacent_cells:
        if board[next_r][next_c] in node.children:
            dfs(next_r, next_c, board, node.children[board[next_r][next_c]])
    board[r][c] = temp # mark as unvisited

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def find_all_words_on_a_board(board: List[List[str]],
                                  words: List[str]) -> List[str]:
        root = ListNode()
        # insert every word into trie
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        res = []
        # start a DFS call from each cell of board that contains a child of root node,
        # which represents the first letter of a word in the trie
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    dfs(board, r, c, root.children[board[r][c]], res)
        return res

    def dfs(board: List[List[str]], r: int, c: int,
            node: TrieNode, res: List[str]) -> None:
        # if current node represents end of a word, add the word to result
        if node.word:
            res.append(node.word)
            # ensure current word is only added once
            node.word = None
        temp = board[r][c]
        # mark current cell as visited
        board[r][c] = '#'
        # explore all adjacent cells that correspond with a child of current TrieNode
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in dirs:
            next_r, next_c = r + d[0], c + d[1]
            if (is_within_bounds(next_r, next_c, board) and board[next_r][next_c] in node.children):
                dfs(board, next_r, next_c, node.children[board[next_r][next_c]], res)
        # backtrack by reverting cell back to its original character
        board[r][c] = temp

    def is_within_bounds(r: int, c: int, board: List[str]) -> bool:
        return 0 <= r < len(board) and 0 <= c < len(board[0])
```

<!-- TOC --><a name="char-13-graphs"></a>

# Char 13 Graphs

```python
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def dfs(node: GraphNode, visited: Set[GraphNode]):
    visited.add(node)
    process(node)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)

def bfs(node: GraphNode):
    visited = set()
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            process(node)
            for neighbor in node.neighbors:
                queue.append(neighbor)
```

<!-- TOC --><a name="graph-deep-copy"></a>

## Graph Deep Copy

```python
def graph_deep_copy(node: GraphNode) -> GraphNode:
    if not node:
        return None
    return dfs(node)

def dfs(node: GraphNode, clone_map = {}) -> GraphNode:
    # if node cloned, return this previously cloned node
    if node in clone_map:
        return clone_map[node]
    # clone current node
    cloned_node = GraphNode(node.val)
    # store current clone to ensure it doesn't need to be created again in future DFS calls
    clone_map[node] = cloned_node
    # iterate through neighbors of current node to connect their clones to current cloned node
    for neighbor in node.neighbors:
        cloned_neighbor = dfs(neighbor, clone_map)
        cloned_node.neighbors.append(cloned_neighbor)
    return cloned_node
```

<!-- TOC --><a name="count-islands"></a>

## Count Islands

```python
def count_islands(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            # if land cell is found, perform DFS to explore full island, and include this island in the count
            if matrix[r][c] == 1:
                dfs(r, c, matrix)
                count += 1
        return count

def dfs(r: int, c: int, matrix: List[List[int]]) -> None:
    # mark current land cell as visited
    matrix[r][c] = -1
    # define direction vectors for up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # recursively call DFS on each neighboring land cell to continue exploring this island
    for d in dirs:
        next_r, next_c = r + d[0], c + d[1]
        if (is_within_bounds(next_r, next_c, matrix) and matrix[next_r][next_c] == 1):
            dfs(next_r, next_c, matrix)

def is_within_bounds(r: int, c: int, matrix: List[List[int]]) -> bool:
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
```

<!-- TOC --><a name="matrix-infection"></a>

## Matrix Infection

```python
def matrix_infection(matrix: List[List[int]]) -> int:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    ones = seconds = 0
    # count total number of uninfected cells and add each infected cell to the queue
    # to represent level 0 of level-order traversal
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                ones += 1
            elif matrix[r][c] == 2:
                queue.append((r, c))
    # use level-order traversal to determine how long it takes to infect uninfected cells
    while queue and ones > 0:
        # 1 second passes with each level of matrix that's explored
        seconds += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            # infect any neighboring 1s and add them to queue to be processed in next level
            for d in dirs:
                next_r, next_c = r + d[0], c + d[1]
                if (is_within_bounds(next_r, next_c, matrix) and matrix[next_r][next_c] == 1):
                    matrix[next_r][next_c] = 2
                    ones -= 1
                    queue.append((next_r, next_c))
    # if still uninfected cells left, return -1. Else, return time passed
    return seconds if ones == 0 else -1

def is_within_bounds(r: int, c: int, matrix: List[List[int]]) -> bool:
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
```

<!-- TOC --><a name="bipartite-graph-validation"></a>

## Bipartite Graph Validation

```python
def bipartite_graph_validation(graph: List[List[int]]) -> bool:
    colors = [0] * len(graph)
    # determine if each graph component is bipartite
    for i in range(len(graph)):
        if colors[i] == 0 and not dfs(i, 1, graph, colors):
            return False
    return True

def dfs(node: int, color: int, graph: List[List[int]], colors: List[int]) -> bool:
    colors[node] = color
    for neighbor in graph[node]:
        # if current neighbor has the same color as the current node, graph is not bipartite
        if colors[neighbor] == color:
            return False
        # if current neighbor is not colored, color it with the other color and continue DFS
        if (colors[neighbor] == 0 and not dfs(neighbor, -color, graph, colors)):
            return False
    return True
```

<!-- TOC --><a name="longest-increasing-path"></a>

## Longest Increasing Path

```python
def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    res = 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    # find longest increasing path starting at each cell
    # max of these = overall longest increasing path
    for r in range(m):
        for c in range(n):
            res = max(res, dfs(r, c, matrix, memo))
    return res

def dfs(r: int, c: int, matrix: List[List[int]], memo: List[List[int]]) -> int:
    if memo[r][c] != 0:
        return memo[r][c]
    max_path = 1
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # longest path starting at current cell = longest path of its larger neighboring cells + 1
    for d in dirs:
        next_r, next_c = r + d[0], c + d[1]
        if (is_within_bounds(next_r, next_c, matrix) and matrix[next_r][next_c] > matrix[r][c]):
            max_path = max(max_path, 1 + dfs(next_r, next_c, matrix, memo))

    memo[r][c] = max_path
    return max_path

def is_within_bounds(r: int, c: int, matrix: List[List[int]]) -> bool:
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
```

<!-- TOC --><a name="shortest-transformation-sequence"></a>

## Shortest Transformation Sequence

```python
def shortest_transformation_sequence(start: str, end: str, dictionary: List[str]) -> int:
    dictionary_set = set(dictionary)
    if start not in dictionary_set or end not in dictionary_set:
        return 0
    if start == end:
        return 1
    lower_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    queue = deque([start])
    visited = set([start])
    dist = 0
    # use level-order traversal to find shortest path from the start word to the end word
    while queue:
        for _ in range(len(queue)):
            curr_word = queue.popleft()
            # if found end word, we've reached it via shortest path
            if curr_word == end:
                return dist + 1
            # generate all possible words that have a one-letter difference to the current word
            for i in range(len(curr_word)):
                for c in lower_case_alphabet:
                    next_word = curr_word[:i] + c + curr_word[i + 1:]
                    # if next_word exists in dictionary, it's a neighbor of current word
                    # if unvisited, add it to the queue to be processed in the next level
                    if (next_word in dictionary_set and next_word not in visited):
                        visited.add(next_word)
                        queue.append(next_word)
        dist += 1
    # if no way to reach the end node, then no path exists
    return 0
```

<!-- TOC --><a name="optimization-bidirectional-traversal"></a>

## Optimization - Bidirectional Traversal

```python
def shortest_transformation_sequence_optimized(start: str, end: str, dictionary: List[str]) -> int:
    dictionary_set = set(dictionary)
    if start not in dictionary_set or end not in dictionary_set:
        return 0
    if start == end:
        return 1
    start_queue = deque([start])
    start_visited = {start}
    end_queue = deque([end])
    end_visited = {end}
    level_start = level_end = 0
    # perform level-order traversal from the start word and another from the end word
    while start_queue and end_queue:
        # explore next level of traversal that starts from the start word
        # if meet the other traversal, shortest path between 'start' and 'end' has been found
        level_start += 1
        if explore_level(start_queue, start_visited, end_visited, dictionary_set):
            return level_start + level_end + 1
        # explore next level of traversal that starts from end word
        level_end += 1
        if explore_level(end_queue, end_visited, start_visited, dictionary_set):
            return level_start + level_end + 1
    # if traversals never met, no path exists
    return 0

# explore next level in the level-order traversal and check if 2 searches meet
def explore_level(queue, visited, other_visited, dictionary_set) -> bool:
    lower_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(len(queue)):
        current_word = queue.popleft()
        for i in range(len(current_word)):
            for c in lower_case_alphabet:
                next_word = current_word[:i] + c + current_word[i + 1:]
                # if next_word has been visited during the other traversal, then both searches have met
                if next_word in other_visited:
                    return True
                if (next_word in dictionary_set and next_word not in visited):
                    visited.add(next_word)
                    queue.append(next_word)
    # if no word has been visited by the other traversal, searches have not met yet
    return False
```

<!-- TOC --><a name="merging-communities"></a>

## Merging Communities

```python
def find(x: int) -> int:
    # if x == parent, found representative
    if x == parent[x]:
        return x
    # else, continue traversing through x's parent chain
    # path compression: updates the representative of x, flattening structure of community
    parent[x] = find(parent[x])
    return parent[x]

def union(x: int, y: int) -> None:
    rep_x, rep_y = find(x), find(y)
    if rep_x != rep_y:
        # if rep_x represents a larger community, connect rep_y's community to it
        if size[rep_x] > size[rep_y]:
            parent[rep_y] = rep_x
            size[rep_x] += size[rep_y]
        # if rep_y represents a larger community or both communities are of the same size, connect rep_x's community to it
        else:
            parent[rep_x] = rep_y
            size[rep_y] += size[rep_x]

class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, x: int, y: int) -> None:
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            # if rep_x represents a larger community, connect rep_y's community to it
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            # otherwise, connect rep_x's community to rep_y
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        # path compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]

class MergingCommunities:
    def __init__(self, n: int):
        self.uf = UnionFind(n)
    def connect(self, x: int, y: int) -> None:
        self.uf.union(x, y)
    def get_community_size(self, x: int) -> int:
        return self.uf.get_size(x)
```

<!-- TOC --><a name="prerequisites"></a>

## Prerequisites

```python
def prerequisites(n: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    in_degrees = [0] * n
    # represent the graph as an adjacency list and record the in-degree of each course.
    for prerequisite, course in prerequisites:
        graph[prerequisite].append(course)
        in_degrees[course] += 1
    queue = deque()
    # add all courses with an in-degree of 0 to the queue
    for i in range(n):
        if in_degrees[i] == 0:
            queue.append(i)
    enrolled_courses = 0
    # perform topological sort
    while queue:
        node = queue.popleft()
        enrolled_courses += 1
        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            # if in-degree of a neighboring course = 0, add it to the queue
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)
    # return true if we've enrolled in all courses
    return enrolled_courses == n
```

## Shortest Path

```python
def shortest_path(n: int, edges: List[int], start: int) -> List[int]:
    graph = defaultdict(list)
    distances = [float('inf')] * n
    distances[start] = 0
    # represent graph as adjacency list
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    min_heap = [(0, start)] # (distance, node)
    # use dijkstra's algo to find shortest path between start node and all other nodes
    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)
        # if current distance to this node > recorded distance, we found the shortest distance to this node
        if curr_dist > distances[curr_node]:
            continue
        # update distances of neighboring nodes
        for neighbor, weight in graph[curr_node]:
            neighbor_dist = curr_dist + weight
            # only update distance if we find shorter path to neighbor
            if neighbor_dist < distances[neighbor]:
                distances[neighbor] = neighbor_dist
                heapq.heappush(min_heap, (neighbor_dist, neighbor))
    return [-1 if dist == float('inf') else dist for dist in distances]
```

## Connect Dots

```python
def connect_the_dots(points: List[List[int]]) -> int:
    n = len(points)
    # create and populate array containing all possible edges
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            # manhattan distance
            cost = (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
            edges.append((cost, i, j))
    # sort edges by cost in ascending order
    edges.sort()
    uf = UnionFind(n)
    total_cost = edges_added = 0
    # use Kruskal algo to create MST and identify its min cost
    for cost, p1, p2 in edges:
        # if points not already connected, connect them, and add cost to total cost
        if uf.union(p1, p2):
            total_cost += cost
            edges_added += 1
            # if n - 1 edges have been added to MST, MST complete
            if edges_added == n - 1:
                return total_cost

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, x, y) -> bool:
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x != rep_y:
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]
            # return True if both groups are merged
            return True
        # return False if points belong to same group
        return False

    def find(self, x) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
```

<!-- TOC --><a name="char-14-backtracking"></a>

# Char 14 Backtracking

```python
def dfs(state):
    # termination condition
    if meets_termination_condition(state):
        process_solution(state)
        return
    # explore each possible decision that can be made at the current state
    for decision in possible_decisions(state):
        make_decision(state, decision)
        dfs(state)
        undo_decision(state, decision) # backtrack
```

<!-- TOC --><a name="find-all-permutations"></a>

## Find All Permutations

```python
def find_all_permutations(nums: List[int]) -> List[List[int]]:
    res = []
    backtrack(nums, [], set(), res)
    return res

def backtrack(nums: List[int], candidate: List[int], used: Set[int], res: List[List[int]]) -> None:
    # if current candidate is complete permutation, add it to result
    if len(candidate) == len(nums):
        res.append(candidate[:])
        return
    for num in nums:
        if num not in used:
            # add num to current permutation and mark it as used
            candidate.append(num)
            used.add(num)
            # recursively explore all branches using updated permutation candidate
            backtrack(nums, candidate, used, res)
            # backtrack by reversing changes made
            candidate.pop()
            used.remove(num)
```

<!-- TOC --><a name="find-all-subsets"></a>

## Find All Subsets

```python
def find_all_subsets(nums: List[int]) -> List[List[int]]:
    res = []
    backtrack(0, [], nums, res)
    return res

def backtrack(i: int, curr_subset: List[int], nums: List[int], res: List[List[int]]) -> None:
    # base case: if all elements have been considered, add current subset to the output
    if i == len(nums):
        res.append(curr_subset[:])
        return
    # include current element and recursively explore all paths that branch from this subset
    curr_subset.append(nums[i])
    backtrack(i + 1, curr_subset, nums, res)
    # exclude current element and recursively explore all paths that branch from this subset
    curr_subset.pop()
    backtrack(i + 1, curr_subset, nums, res)
```

<!-- TOC --><a name="n-queens"></a>

## N Queens

```python
res = 0

def n_queens(n: int) -> int:
    dfs(0, set(), set(), set(), n)
    return res

def dfs(r: int, diagonals_set: Set[int], anti_diagonals_set: Set[int], cols_set: Set[int], n: int) -> None:
    global res
    # termination condition: if we've reached the end of the rows, we've placed all n queens
    if r == n:
        res += 1
        return
    for c in range(n):
        curr_diagonal = r - c
        curr_anti_diagonal = r + c
        # if queens on current column, diagonal or anti-diagonal, skip this square
        if (c in cols_set or curr_diagonal in diagonals_set or curr_anti_diagonal in anti_diagonals_set):
            continue
        # place queen by marking current column, diagonal, and anti-diagonal as occupied
        cols_set.add(c)
        diagonals_set.add(curr_diagonal)
        anti_diagonals_set.add(curr_anti_diagonal)
        # recursively move to the next row to continue placing queens
        dfs(r + 1, diagonals_set, anti_diagonals_set, cols_set, n)
        # backtrack by removing the current column, diagonal and anti-diagonal from hash sets
        cols_set.remove(c)
        diagonals_set.remove(curr_diagonal)
        anti_diagonals_set.remove(curr_anti_diagonal)
```

## Combinations of a Sum

```python
def combinations_of_sum_k(nums: List[int], target: int) -> List[List[int]]:
    res = []
    dfs([], 0, nums, target, res)
    return res

def dfs(combination: List[int], start_index: int, nums: List[int], target: int,
        res: List[List[int]]) -> None:
    # termination condition: if target == 0, found a combination that sums to k
    if target == 0:
        res.append(combination[:])
        return
    # termination condition: if target < 0, no mode valid combinations can be
    if target < 0:
        return
    # starting from start_index, explore all combinations after adding nums[i]
    for i in range(start_index, len(nums)):
        # add current number to create new combination
        combination.append(nums[i])
        # recursively explore all paths that branch from this new combination
        dfs(combination, i, nums, target - nums[i], res)
        # backtrack by removing number we just added
        combination.pop()
```

## Phone Keypad Combinations

```python
def phone_keypad_combinations(digits: str) -> List[str]:
    keypad_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    res = []
    backtrack(0, [], digits, keypad_map, res)
    return res

def backtrack(i: int, curr_combination: List[str], digits: str,
              keypad_map: Dist[str, str], res: List[str]) -> None:
    # termination condition: if all digits considered, add current combination to output list
    if len(curr_combination) == len(digits):
        res.append("".join(curr_combination))
        return
    for letter in keypad_map[digits[i]]:
        # add current letter
        curr_combination.append(letter)
        # recursively explore all paths that branch from this combination
        backtrack(i + 1, curr_combination, digits, keypad_map, res)
        # backtrack by removing letter we just added
        curr_combination.pop()
```

<!-- TOC --><a name="char-15-dynamic-programming"></a>

# Char 15 Dynamic Programming

<!-- TOC --><a name="climbing-stairs"></a>

## Climbing Stairs

<!-- TOC --><a name="top-down"></a>

### Top-down

```python
memo = {}
def climbing_stairs_top_down(n: int) -> int:
    # base case: with a 1-step staircase, there's only one way to climb it, 2-step staircase, 2 ways.
    if n <= 2:
        return n
    if n in memo:
        return memo[n]
    # number of ways to climb to n-th step = sum of number of ways to climb to step n - 1 and to n - 2
    memo[n] = (climbing_stairs_top_down(n - 1) + climbing_stairs_top_down(n - 2))
    return memo[n]
```

<!-- TOC --><a name="botom-up"></a>

### Botom-up

```python
def climbing_stairs_bottom_up(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    # base case
    dp[1], dp[2] = 1, 2
    # starting from step 3, calculate number of ways to reach each step until the n-th step
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

<!-- TOC --><a name="optimization-bottom-up"></a>

### Optimization - bottom up

```python
def climbing_stairs_bottom_up_optimized(n: int) -> int:
    if n <= 2:
        return n
    # set one-step-before and two-steps-before as base cases
    one_step_before, two_steps_before = 2, 1
    for i in range(3, n + 1):
        # calculate number of ways to reach current step
        current = one_step_before + two_steps_before
        # update values for next iteration
        two_steps_before = one_step_before
        one_step_before = current
    return one_step_before
```

<!-- TOC --><a name="min-coin-combination"></a>

## Min Coin Combination

<!-- TOC --><a name="top-down-1"></a>

### Top Down

```python
def min_coin_combination_top_down(coins: List[int], target: int) -> int:
    res = top_down_dp(coins, target, {})
    return -1 if res == float('inf') else res

def top_down_dp(coins: List[int], target: int, memo: Dict[int, int]) -> int:
    # base case: if target = 0, then 0 coins are needed to reach it
    if target == 0:
         return 0
    if target in memo:
        return memo[target]
    # initialize min_coins to a large number
    min_coins = float('inf')
    for coin in coins:
        # avoid negative targets
        if coin <= target:
            # calculate min number of coins needed if we use current coin
            min_coins = min(min_coins, 1 + top_down_dp(coins, target - coin, memo))
    memo[target] = min_coins
    return memo[target]
```

<!-- TOC --><a name="bottom-up"></a>

### Bottom up

```python
def min_coin_combination_bottom_up(coins: List[int], target: int) -> int:
    # DP array will store min number of coins needed for each amount
    # set each element to a large number initially
    dp = [float('inf')] * (target + 1)
    # base case: if target = 0, 0 coins are needed
    dp[0] = 0
    # update DP array for all target amounts > 0
    for t in range(1, target + 1):
        for coin in coins:
            if coin <= t:
                dp[t] = min(dp[t], 1 + dp[t - coin])
    return dp[target] if dp[target] != float('inf') else -1
```

<!-- TOC --><a name="matrix-pathways"></a>

## Matrix Pathways

```python
def matrix_pathways(m: int, n: int) -> int:
    # base case: set all cells in row 0 and column 0 to 1, initialize all cells in dp table to 1
    dp = [[1] * n for _ in range(m)]
    # fill in the rest of DP table
    for r in range(1, m):
        for c in range(1, n):
            # paths to current cell = paths from above + paths from left
            dp[r][c] = dp[r -1][c] + dp[r][c - 1]
    return dp[m - 1][n - 1]
```

<!-- TOC --><a name="optimized-1"></a>

### Optimized

```python
def matrix_pathways_optimized(m: int, n: int) -> int:
    # initialize prev_row as DP values of row 0, which are all 1s.
    prev_row = [1] * n
    # iterate through matrix starting from row 1
    for r in range(1, m):
        # set first cell of curr_row to 1, by setting entire row to 1
        curr_row = [1] * n
        for c in range(1, n):
            # number of unique paths to current cell is the sum of paths from the cell above it (prev_row[c])
            # and the cell to the left curr_row[c - 1]
            curr_row[c] = prev_row[c] + curr_row[c - 1]
        # update prev_row with curr_row values for the next iteration
        prev_row = curr_row
    # last element in prev_row stores the result for bottom_right cell
    return prev_row[n - 1]
```

<!-- TOC --><a name="neighborhood-burglary"></a>

## Neighborhood Burglary

```python
def neighborhood_burglary(houses: List[int]) -> int:
    # handle cases when size of array < 2 to avoid out-of-bounds errors when assigning base case values
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    dp = [0] * len(houses)
    # base case: when only 1 house, rob it
    dp[0] = houses[0]
    # base case: when only 2 houses, rob the most money one
    dp[1] = max(houses[0], houses[1])
    # fill in the rest of DP array
    for i in range(2, len(houses)):
        # dp[i] = max(profit if we skip house i, profit if we rob house i)
        dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])
    return dp[len(houses) - 1]
```

<!-- TOC --><a name="optimization"></a>

### Optimization

```python
def neighborhood_burglary_optimized(houses: List[int]) -> int:
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    # initialize variables with base cases
    prev_max_profit = max(houses[0], houses[1])
    prev_prev_max_profit = houses[0]
    for i in range(2, len(houses)):
        curr_max_profit = max(prev_max_profit, houses[i] + prev_prev_max_profit)
        # update values for next iteration
        prev_prev_max_profit = prev_max_profit
        prev_max_profit = curr_max_profit
    return prev_max_profit
```

<!-- TOC --><a name="longest-common-subsequence-lcs"></a>

## Longest Common Subsequence (LCS)

```python
def longest_common_subsequence(s1: str, s2: str) -> int:
    # base case: set last row and last column to 0 by initializing entire DP table with 0s.
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    # populate DP table
    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            # if character match, length of LCS at dp[i][j] is 1 + LCS length of remaining substrings
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            # if characters don't match, LCS length at dp[i][j] can be found by either
            # 1. excluding current character of s1
            # 2. excluding current character of s2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]
```

<!-- TOC --><a name="optimization-1"></a>

### Optimization

```python
def longest_common_subsequence_optimized(s1: str, s2: str) -> int:
    # initialize prev_row as DP values of the last row
    prev_row = [0] * (len(s2) + 1)
    for i in range(len(s1) - 1, -1, -1):
        # set last cell of curr_row to 0 to set base case for this row
        # by initializing entire row to 0
        curr_row = [0] * (len(s2) + 1)
        for j in range(len(s2) - 1, -1, -1):
            # if characters match, length of LCS at curr_row[j] is 1 + LCS length of remaining substrings prev_row[j + 1]
            if s1[i] == s2[j]:
                curr_row[j] = 1 + prev_row[j + 1]
            # if characters don't match, length of LCS at curr_row[j] can be found by either
            # 1. excluding current character of s1 = prev_row[j]
            # 2. excluding current character of s2 = curr_row[j + 1]
            else:
                curr_row[j] = max(prev_row[j], curr_row[j + 1])
        # update prev_row with curr_row values for next iteration
        prev_row = curr_row
    return prev_row[0]
```

<!-- TOC --><a name="longest-palindrome-in-string"></a>

## Longest Palindrome in String

```python
def longest_palindrome_in_a_string(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    dp = [[False] * n for _ in range(n)]
    max_len = 1
    start_index = 0
    # base case: single character is always palindrome
    for i in range(n):
        dp[i][i] = True
    # Base case: substring of length 2 is a palindrome if both characters are same
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] == True
            max_len = 2
            start_index = i
    # find palindrome substrings of length 3 or greater
    for substring_len in range(3, n + 1):
        # iterate through each substring of length substring_len
        for i in range(n - substring_len + 1):
            j = i + substring_len - 1
            # if first and last characters are the same, and inner substring is palindrome, then it's palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                max_len = substring_len
                start_index = i
    return s[start_index: start_index + max_len]

# expand outward from the center of a base case to identify start index and length of longest palindrome that extends from base case
def expand_palindrome(left: int, right: int, s: str) -> Tuple[int, int]:
    while (left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]):
        left -= 1
        right += 1
    return left, right - left + 1
```

<!-- TOC --><a name="max-subarray-sum"></a>

## Max Subarray Sum

```python
def max_subarray_sum(nums: List[int]) -> int:
    if not nums:
        return 0
    # set num variables to -infinity to ensure negative sums can be considered
    max_sum = current_sum = float('-inf')
    # iterate through array to find max subarray sum
    for num in nums:
        # either add current number to existing running sum, or start new subarray at current number
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def max_subarray_sum_dp(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp = [0] * n
    # base case: max subarray sum of an array with 1 element is that element
    dp[0] = nums[0]
    max_sum = dp[0]
    # populate rest of DP array
    for i in range(1, n):
        # determine max subarray sum ending at current index
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])
    return max_sum

def max_subarray_sum_dp_optimized(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    current_sum = nums[0]
    max_sum = nums[0]
    for i in range(1, n):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
```

<!-- TOC --><a name="01-knapsack"></a>

## 0-1-knapsack

```python
def knapsack(cap: int, weights: List[int], values: List[int]) -> int:
    n = len(values)
    # base case: set first column and last row to 0 by initializing entire DP table to 0
    dp = [[0 for x in range(cap + 1)] for x in range(n + 1)]
    # populate DP table
    for i in range(n - 1, -1, -1):
        for c in range(1, cap + 1):
            # if item i fits in current knapsack capacity, max value at dp[i][c] is the largest of either:
            # 1. max value if include item i
            # 2. max value if exclude item i
            if weights[i] <= c:
                dp[i][c] = max(values[i] + dp[i + 1][c - weights[i]], dp[i + 1][c])
        # if doesn't fit, we have to exclude it
        else:
            dp[i][c] = dp[i + 1][c]
    return dp[0][cap]

def knapsack_optimized(cap: int, weights: List[int], values: List[int]) -> int:
    n = len(values)
    # initialize prev_row as DP values of row below current row
    prev_row = [0] * (cap + 1)
    for i in range(n - 1, -1, -1):
        # set first cell of curr_row to 0 to set the base case for this row, by initializing entire row to 0
        curr_row = [0] * (cap + 1)
        for c in range(1, cap + 1):
            # if item i fits in current knapsack capacity, max value at curr_row[c] is the largest of either
            # 1. max value if include item i
            # 2. max value if exclude item i
            if weights[i] <= c:
                curr_row[c] = max(values[i] + prev_row[c - weights[i]], prev_row[c])
            # if item i doesn't fit, exclude
            else:
                curr_row[c] = prev_row[c]
        # set prev_row to curr_row values for next iteration
        prev_row = curr_row
    return prev_row[cap]
```

## Largest Square in Matrix

```python
def largest_square_in_matrix(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_len = 0
    # base case: if cell in row 0 is 1, largest square ending there has a length of 1
    for j in range(n):
        if matrix[0][j] == 1:
            dp[0][j] = 1
            max_len = 1
    # base case: if cell in column 0 is 1, largest square ending there has a length of 1
    for i in range(m):
        if matrix[i][0] == 1:
            dp[i][0] = 1
            max_len = 1
    # populate the rest of DP table
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                # length of largest square ending here is determined by smallest square ending at
                # neighboring cells (left, top - left, top) + 1 to include this cell
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
            max_len = max(max_len, dp[i][j])
    return max_len ** 2
```

### Optimization

```python
def largest_square_in_matrix_optimized(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    prev_row = [0] * n
    max_len = 0
    # iterate through matrix
    for i in range(m):
        curr_row = [0] * n
        for j in range(n):
            # base case: if in row 0 or column 0, largest square ending here has length of 1
            # this can be set by using value in input matrix
            if i == 0 or j == 0:
                curr_row[j] = matrix[i][j]
            else:
                if matrix[i][j] == 1:
                    # curr_row[j] = 1 + min(left, top - left, top)
                    curr_row[j] = 1 + min(curr_row[j - 1], prev_row[j - 1], prev_row[j])
            max_len = max(max_len, curr_row[j])
        # update prev_row with curr_row values for next iteration
        prev_row, curr_row = curr_row, [0] * n
    return max_len ** 2
```

<!-- TOC --><a name="char-16-greedy"></a>

# Char 16 Greedy

<!-- TOC --><a name="jump-to-end"></a>

## Jump to End

```python
def jump_to_the_end(nums: List[int]) -> bool:
    # set initial destination to the last index in array
    destination = len(nums) - 1
    # traverse array in reverse to see if destination can be reached by earlier indexes
    for i in range(len(nums) - 1, -1, -1):
        # if reach destination from current index, set this index as new destination
        if i + nums[i] >= destination:
            destination = i
    # if destination is index 0, we can jump to end from index 0
    return destination == 0
```

<!-- TOC --><a name="gas-stations"></a>

## Gas Stations

```python
def gas_stations(gas: List[int], cost: List[int]) -> int:
    # if total gas < total cost, completing circuit is impossible
    if sum(gas) < sum(cost):
        return -1
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        # if tank gas < 0, can't continue through circuit from current start point,
        # nor from any station before or including current station i
        if tank < 0:
            # set next station as new start point and reset tank
            start, tank = i + 1, 0
    return start
```

<!-- TOC --><a name="candies"></a>

## Candies

```python
def candies(ratings: List[int]) -> int:
    n = len(ratings)
    # ensure each child starts with 1 candy
    candies = [1] * n
    # first pass: for each child, ensure child has more candies than their left-side neighbor if current child's rating is higher
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    # second pass: for each child, ensure child has more candies than their right-side neighbor if current child's rating is higher
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            # if current child already has more candies than their right-side neighbor, keep higher amount
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)
```

<!-- TOC --><a name="char-17-sort-and-search"></a>

# Char 17 Sort and Search

<!-- TOC --><a name="sort-linked-list"></a>

## Sort Linked List

```python
def merge_sort(head):
    # split linked list into 2 halves
    second_head = split_list(head)
    # recursively sort both halves
    first_half_sorted = merge_sort(head)
    second_half_sorted = merge_sort(second_head)
    # merge sorted sublists
    return merge(first_half_sorted, second_half_sorted)

def sort_linked_list(head: ListNode) -> ListNode:
    # if linked list empty or has only 1 element, it's already sorted
    if not head or not head.next:
        return head
    # split linked list into halves using fast and slow pointer
    second_head = split_list(head)
    # recursively sort both halves
    first_half_sorted = sort_linked_list(head)
    second_half_sorted = sort_linked_list(second_head)
    # merge sorted sublists
    return merge(first_half_sorted, second_half_sorted)

def split_list(head: ListNode) -> ListNode:
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second_head = slow.next
    slow.next = None
    return second_head

def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    # pointer will be used to append nodes to tail of the merged linked list
    tail = dummy
    # continually append node with smaller value from each linked list to the merged linked list until
    # one of the linked lists has no more nodes to merge
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    # one of 2 linked lists could still have nodes remaining, attach them to the end of merged linked list
    tail.next = l1 or l2
    return dummy.next
```

<!-- TOC --><a name="sort-array"></a>

## Sort Array

```python
def quicksort(nums, left, right):
    # partition the array and obtain index of pivot
    pivot_index = partition(nums, left, right)
    # sort left and right parts
    quicksort(nums, left, pivot_index - 1)
    quicksort(nums, pivot_index + 1, right)

def sort_array(nums: List[int]) -> List[int]:
    quicksort(nums, 0, len(nums) - 1)
    return nums

def quicksort(nums: List[int], left: int, right: int) -> None:
    # base case: if subarray has 0 or 1 element, it's already sorted
    if left >= right:
        return
    # partition the array and retrieve pivot index
    pivot_index = partition(nums, left, right)
    # call quicksort on left and right parts to recursively sort them
    quicksort(nums, left, pivot_index - 1)
    quicksort(nusm, pivot_index + 1, right)

def partition(nums: List[int], left: int, right: int) -> int:
    pivot = nums[right]
    lo = left
    # move all numbers < pivot to the left, which consequently positions all numbers >= pivot to the right
    for i in range(left, right):
        if nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
    # after partitioning, lo will be positioned where pivot should be, so swap the pivot number with the number at lo pointer
    nums[lo], nums[right] = nums[right], nums[lo]
    return lo

def quicksort_optimized(nums: List[int], left: int, right: int) -> None:
    if left >= right:
        return
    # choose pivot at random index
    random_index = random.randint(left, right)
    # swap randomly chosen pivot with rightmost element to position the pivot at rightmost index
    nums[random_index], nums[right] = nums[right], nums[random_index]
    pivot_index = partition(nums, left, right)
    quicksort_optimized(nums, left, pivot_index - 1)
    quicksort_optimized(nums, pivot_index + 1, right)

def sort_array_counting_sort(nums: List[int]) -> List[int]:
    if not nums:
        return []
    res = []
    # count occurrences of each element in nums
    counts = [0] * (max(nums) + 1)
    for num in nums:
        counts[num] += 1
    # build sorted array by appending each index i to it a total of counts[i] times
    for i, count in enumerate(counts):
        res.extend([i] * count)
    return res
```

<!-- TOC --><a name="k-th-largest-integer"></a>

## K-th Largest Integer

```python
def kth_largest_integer_min_heap(nums: List[int], k: int) -> int:
    min_heap = []
    heapq.heapify(min_heap)
    for num in nums:
        # ensure heap has at least k integers
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        # if num > smallest integer in the heap, pop off this smallest integer from the hap and push in num
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return min_heap[0]
```

<!-- TOC --><a name="quickselect"></a>

### Quickselect

```python
def kth_largest_integer_quickselect(nums: List[int], k: int) -> int:
    return quickselect(nums, 0, len(nums) - 1, k)

def quickselect(nums: List[int], left: int, right: int, k: int) -> None:
    n = len(nums)
    if left >= right:
        return nums[left]
    random_index = random.randint(left, right)
    nums[random_index], nums[right] = nums[right], nums[random_index]
    pivot_index = partition(nums, left, right)
    # if pivot comes before n - k, the n-k th smallest integer is somewhere to its right
    # perform quickselect on the right part
    if pivot_index < n - k:
        return quickselect(nums, pivot_index + 1, right, k)
    # if pivot comes after n - k, the n-k th smallest integer is somewhere to its left
    # perform quickselect on the left part
    elif pivot_index > n - k:
        return quickselect(nums, left, pivot_index - 1, k)
    # if pivot at index n - k, it's the n-k the smallest integer
    else:
        return nums[pivot_index]

def partition(nums: List[int], left: int, right: int) -> int:
    pivot = nums[right]
    lo = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
    nums[lo], nums[right] = nums[right], nums[lo]
    return lo
```

## Dutch National Flag

```python
def dutch_national_flag(nums: List[int]) -> None:
    i, left, right = 0, 0, len(nums) - 1
    while i <= right:
        # swap 0s with element at the left pointer
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        # swap 2s with element at the right pointer
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1
```

<!-- TOC --><a name="char-18-bit-manipulation"></a>

# Char 18 Bit Manipulation

<!-- TOC --><a name="hamming-weights-of-integers"></a>

## Hamming Weights of Integers

```python
def hamming_weights_of_integers(n: int) -> List[int]:
    return [count_set_bits(x) for x in range(n + 1)]

def count_set_bits(x: int) -> int:
    count = 0
    # count each set bit of x until x = 0
    while x > 0:
        # increment count if LSB is 1
        count += x & 1
        # right shift x to shift the next bit to LSB position
        x >>= 1
    return count

def hamming_weights_of_integers_dp(n: int) -> List[int]:
    # base case: number of set bits in 0 is 0. Set dp[0] = 0 by initializing entire DP array to 0
    dp = [0] * (n + 1)
    for x in range(1, n + 1):
        # dp[x] is obtained using result of dp[x >> 1], plus LSB of x
        dp[x] = dp[x >> 1] + (x & 1)
    return dp
```

<!-- TOC --><a name="lonely-integer"></a>

## Lonely Integer

```python
def lonely_integer(nums: List[int]) -> int:
    res = 0
    # XOR each element of array so that duplicate values will cancel each other out
    # x ^ x == 0
    for num in nums:
        res ^= num
    # res stores the lonely integer because it won't have been canceled out by any duplicat
    return res
```

<!-- TOC --><a name="swap-odd-and-even-bits"></a>

## Swap Odd and Even Bits

```python
def swap_odd_and_even_bits(n: int) -> int:
    even_mask = 0x5555555
    odd_mask = 0xAAAAAAA
    even_bits = n & even_mask
    odd_bits = n & odd_mask
    # shift even bits to the left, odd bits to the right, and merge these shifted values together
    return (even_bits << 1) | (odd_bits >> 1)
```

<!-- TOC --><a name="char-19-math-and-geometry"></a>

# Char 19 Math and Geometry

<!-- TOC --><a name="spiral-traversal"></a>

## Spiral Traversal

```python
def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    result = []
    # initialize matrix boundaries
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    # traverse matrix in spiral order
    while top <= bottom and left <= right:
        # move from left to right along the top boundary
        for i in range(left, right + 1):
            result.append(matrix[top][1])
        top += 1
        # move from top to bottom along the right boundary
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        # check bottom boundary hasn't passed the top boundary before moving from right to left along the bottom boundary
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        # check left boundary hasn's passed the right boundary before moving from bottom to top along the left boundary
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
```

<!-- TOC --><a name="reverse-32-bit-integer"></a>

## Reverse 32-bit Integer

```python
def reverse_32_bit_integer(n: int) -> int:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    reversed_n = 0
    # keep looping until we've added all digits of n to reversed_n in reverse order
    while n != 0:
        # digit = n % 10
        digit = int(math.fmod(n, 10))
        # n = n // 10
        n = int(n / 10)
        # check for integer overflow or underflow
        if (reversed_n > int(INT_MAX / 10) or reversed_n < int(INT_MIN / 10)):
            return 0
        # add current digit to reversed_n
        reversed_n = reversed_n * 10 + digit
    return reversed_n
```

<!-- TOC --><a name="max-collinear-points"></a>

## Max Collinear Points

```python
def max_collinear_points(points: List[List[int]]) -> int:
    res = 0
    # treat each point as focal point, and determine max number of points that are collinear with each focal point
    # largest of these max is the answer
    for i in range(len(points)):
        res = max(res, max_points_from_focal_point(i, points))
    return res

def max_points_from_focal_point(focal_point_index: int, points: List[List[int]]) -> int:
    slopes_map = defaultdict(int)
    max_points = 0
    # for current focal point, calculate slope between it and every other point
    # we can group points that share same slope
    for j in range(len(points)):
        if j != focal_point_index:
            curr_slope = get_slope(points[focal_point_index], points[j])
            slopes_map[curr_slope] += 1
            # update max count of collinear points for current focal point
            max_point = max(max_points, slope_map[curr_slope])
    # add 1 to max count to include focal point itself
    return max_point + 1

def get_slope(p1: List[int], p2: List[int]) -> Tuple[int, int]:
    rise = p2[1] - p1[1]
    run = p2[0] - p1[0]
    # handle vertical lines separately to avoide dividing by 0
    if run == 0:
        return (1, 0)
    # simplify slope to its reduced form
    gcd_val = gcd(rise, run)
    return (rise // gcd_val, run // gcd_val)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

## Josephus Problem

```python
def josephus(n: int, k: int) -> int:
    # base case: if there's only 1 person, last person is person 0
    if n == 1:
        return 0
    # calculate position of last person remaining in reduced probelm with n - 1 people
    # use modulo n to ensure answer not exceed n - 1
    return (josephus(n - 1, k) + k) % n

def josephus_optimized(n: int, k: int) -> int:
    res = 0
    for i in range(2, n + 1):
        # res[i] = (res[i - 1] + k) % i
        res = (res + k) % i
    return res
```

## Triangle Numbers

```python
def triangle_numbers(n: int) -> int:
    # if n is odd, first even number starts at position 2
    if n % 2 != 0:
        return 2
    # if n is multiple of 4, first even number starts at position 3
    elif n % 4 == 0:
        return 3
    # other rows, first even number starts at position 4
    return 4
```

---

# Templates

### 1. Quick Sort

```python
def quick_sort(q: [], l: int, r: int) -> None:
    if l >= r:
        return
    p, i, j = q[l + r >> 1], l - 1, r + 1
    while i < j:
        while 1:
            i += 1
            if q[i] >= p:
                break
        while 1:
            j -= 1
            if q[j] <= p:
                break
        if i < j:
            q[i], q[j] = q[j], q[i]
    quick_sort(q, l, j)
    quick_sort(q, j + 1, r)
```

### 2. Merge Sort

```python
def merge_sort(q, l, r):
    if l >= r:
        return
    mid = l + r >> 1
    merge_sort(q, l, mid)
    merge_sort(q, mid + 1, r)
    i, j = 0, mid + 1
    tmp = list()
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            tmp.append(q[i])
            i += 1
        else:
            tmp.append(q[j])
            j += 1
    while i <= mid:
        tmp.append(q[i])
        i += 1
    while j <= r:
        tmp.append(q[j])
        j += 1
    k = 0
    for i in range(l, r + 1):
        q[i] = tmp[k]
        k += 1
```

### 3. Binary Search

Integer Binary Search

```python
def check(x: int) -> bool:
    return False

# If [l, r] = [l, mid] + [mid + 1, r]
def bsearch_1(l: int, r: int) -> int:
    while l < r:
        mid = l + r >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l

# If [l, r] = [l, mid - 1] + [mid, r]
def bsearch_2(l: int, r: int) -> int:
    while l < r:
        mid = l + r + 1 >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    return l
```

Float Binary Search

```python
def check(x: float) -> bool:
    return False

def bsearch_3(l: float, r: float) -> float:
    eps = 1e-6
    while r - l > eps:
        mid = (l + r) / 2
        if check(mid):
            r = mid
        else:
            l = mid
    return l
```

### 4. Prefix Sum

Sum of (x1, y1), (x2, y2)

```python
s[x2, y2] - s[x1 - 1, y2] - s[x2, y1 - 1] + s[x1 - 1, y1 - 1]
```

### 5. Bit Operation

k-th digit of n

```python
n >> k & 1
```

last 1 of n

```python
lowbit(n) = n & -n
```

### 6. Two Pointers

```python
j = 0
for i in range(n):
    while (j < i and check(i, j)):
        j += 1
        # operations
```

### 7. Merge Intervals

```python
def merge(a: [(int, int)]):
    res = list()
    a.sort(key=lambda x:x[0])
    cur_st, cur_ed = -10 ** 9, -10 ** 9
    for st, ed in a:
        if cur_ed < st:
            if cur_st != -10 ** 9:
                res.append((cur_st, cur_ed))
            cur_st, cur_ed = st, ed
        else:
            cur_ed = max(cur_ed, ed)
    if cur_st != -10 ** 9:
        res.append((cur_st, cur_ed))
    segs = res
```

### 8. Linked List

```python
# e[]: values, ne[]: next pointer, idx: current node
head, e, ne, idx = -1, [0] * n, [0] * n, 0

def init():
    head = -1
    idx = 0

# insert a at head
def insert(a):
    global idx, head
    e[idx] = a
    ne[idx] = head
    head = idx
    idx += 1

# delete head, but make sure head exists
def remove():
    global head
    head = ne[head]
```

Double Linked List

```python
# e[]: value, l[]: left pointer, r[]: right pointer, idx: current node
e, l, r, idx = [0] * n, [0] * n, [0] * n, 0

def init():
    # 0: left, 1: right
    global idx
    r[0] = 1
    l[1] = 0
    idx = 2

# add x right to a
def insert(a: int, x: int):
    global idx
    e[idx] = x
    l[idx] = a, r[idx] = r[a]
    l[r[a]] = idx
    r[a] = idx
    idx += 1

# delete a
def remove(a: int):
    l[r[a]] = l[a]
    r[l[a]] = r[a]
```

### 9. Stack

```python
# tt: top of stack
stk, tt = [0] * n, 0

# add x to top of stack
tt += 1
stk[tt] = x

# pop from top
tt -= 1

# top value
stk[tt]

# check if empty
if tt > 0:
```

Monotone Stack: Find the nearest left number < or > it
`tt = 0 for i in range(1, n + 1)`

```python
while tt and check(stk[tt], i):
    tt -= 1
tt += 1
stk[tt] = i
```

### 10. Queue

```python
# hh: queue head, tt: queue end
q = [0] * n
hh, tt = 0, -1
# add number at queue end
tt += 1
q[tt] = x
# pop a number from head
hh += 1
# queue head value
q[hh]
# check if queue empty
if hh <= tt:
```

Recursive Queue

```python
# hh: queue head, tt: queue end
q = [0] * n
hh, tt = 0, 0
# add number at queue end
q[tt] = x
tt += 1
if tt == n:
    tt = 0
# pop a number from head
hh += 1
if hh == n:
    hh = 0
# queue head value
q[hh]
# check if queue empty
if hh != tt:
```

Monotone Queue: Find the max/min of sliding window
`int hh = 0, tt = -1 for i in range(0, n)`

```python
while hh <= tt and check_out(q[hh]):
    hh += 1 # check if head of queue is out of window
while hh <= tt and check(q[tt], i):
    tt -= 1
tt += 1
q[tt] = i
```

### 11. KMP

```python
# s[]: long text, p[]: pattern string, n: len(s), m: len(p)
```

next array of pattern string

```python
j = 0
for i in range(2, m + 1):
    while j and p[i] != p[j + 1]:
        j = ne[j]
    if p[i] == p[j + 1]:
        j += 1
    ne[i] = j
```

match

```python
j = 0
for i in range(1, n + 1):
    while j and s[i] != p[j + 1]:
        j = ne[j]
    if s[i] == p[j + 1]:
        j += 1
    if j == m:
        j = ne[j]
        # operations
```

### 12. Trie

```python
# int son[N][26]: each node's child node, cnt[N]: each node's number of words, idx
# 0 node is root node and empty node
```

insert string

```python
def insert(s):
    p = 0
    for i in range(len(s)):
        u = ord(s[i]) - ord('a')
        # node not stored
        if not son[p][u]:
            idx += 1
            son[p][u] = idx
        p = son[p][u]
    # number of strings += 1
    cnt[p] += 1
```

count this string

```python
def query(s):
    p = 0
    for i in range(len(s)):
        u = ord(s[i]) - ord('a')
        if not son[p][u]:
            return 0
        p = son[p][u]
    return cnt[p]
```

### 13. Union Find

```python
p = [0] * n # each node's parent
# return x's parent
def find(x: int):
    if p[x] != x:
        # make parent's parent as root node
        p[x] = find(p[x])
    return p[x]

# initialize, node from 1 to n
for i in range(1, n + 1):
    p[i] = i

# union sets a and b
p[find(a)] = find(b)
```

size of root node

```python
# p[]: each node's parent, size[]: number of nodes of root node
p, size = [0] * n, [0] * n
# return x's root
def find(x: int):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

# initialize, nodes from 1 to n
for i in range(1, n + 1):
    p[i] = i
    size[i] = 1

# union sets a and b
size[find(b)] += size[find(a)]
p[find(a)] = find(b)
```

distance from root node

```python
# p[]: each node's root, d[x]: distance(x, p[x])
p, d = [0] * n, [0] * n

# x's root
def find(x: int):
    if p[x] != x:
        u = find(p[x])
        d[x] += d[p[x]]
        p[x] = u
    return p[x]

# initialize, node from 1 to n
for i in range(1, n + 1):
    p[i] = i
    d[i] = 0

# union sets a and b
p[find(a)] = find(b)
d[find(a)] = distance
```

### 14. Heap

```python
# h[N]: values of heap, h[1]: top of heap, x left child = 2x, right child = 2x + 1
# ph[k]: k-th node inserted in heap, hp[k]: order of insertion of node k
h, ph, hp, size = [0] * n, [0] * n, [0] * n, 0
```

swap 2 nodes and mappings

```python
def heap_swap(a: int, b: int):
    ph[hp[a]], ph[hp[b]] = ph[hp[b]], ph[hp[a]]
    hp[a], hp[b] = hp[b], hp[a]
    h[a], h[b] = h[b], h[a]

def down(u: int):
    t = u
    if u * 2 <= size and h[u * 2] < h[t]:
        t = u * 2
    if u * 2 + 1 <= size and h[u * 2 + 1] < h[t]:
        t = u * 2 + 1
    if u != t:
        heap_swap(u, t)
        down(t)

def up(u: int):
    while u / 2 and h[u] < h[u // 2]:
        heap_swap(u, u // 2)
        u >>= 1

# O(n) build heap
for i in range(n // 2, -1, -1):
    down(i)
```

### 15. Hash

```python
h, e, ne, idx = [0] * n, [0] * n, [0] * n, 0

def insert(x: int):
    k = (x % n + n) % n
    e[idx] = x
    ne[idx] = h[k]
    h[k] = idx
    idx += 1

def find(x: int):
    k = (x % n + n) % n
    i = h[k]
    while i != -1:
        if e[i] == x:
            return True
        i = ne[i]
    return False
```

Open address finding

```python
h = [0] * n
null = -10 ** 9

def find(x: int):
    t = (x % n + n) % n
    while h[t] != null and h[t] != x:
        t += 1
        if t == n:
            t = 0
    return t
```

String Hash

See string as a p^k number, p = 131

```python
# h[k]: hash value of first k digits of string, p[k] = p^k mod 2^64
h, p, ma = [0] * n, [0] * n, 2 ** 64
p[0] = 1 # initialize
for i in range(1, n + 1):
    h[i] = (h[i - 1] * P + str[i]) % ma
    p[i] = (p[i - 1] * P) % ma

# substr[l ~ r] hash value
def get(l, r):
    return h[r] - h[l - 1] * p[r - l + 1]
```

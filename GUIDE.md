# Codeforces Problem-Solving Guide for Python

A complete, step-by-step framework for approaching any Codeforces problem in Python—from reading the statement to submitting without TLE.


## Part 1: The Universal Problem-Solving Framework

Every Codeforces problem, regardless of rating, follows the same decision pipeline. Do not touch the keyboard until you finish Steps 1–4.

### Step 1: Read Constraints First (30 seconds)

Before thinking about algorithms, look at `n`'s upper bound. Constraints eliminate most wrong approaches instantly.

| Constraint | Feasible Complexity | Typical Approach |
|------------|---------------------|------------------|
| n ≤ 20 | O(2ⁿ), O(n!) | Bitmask DP, backtracking |
| n ≤ 1,000 | O(n²) | Nested loops, simple DP |
| n ≤ 10⁵ | O(n log n) or O(n) | Sorting, binary search, two pointers, prefix sums |
| n ≤ 10⁶ | O(n) | Single-pass simulation, greedy |

If `n = 2 × 10⁵`, an O(n²) solution is dead on arrival. Write down the target complexity before proceeding.

### Step 2: Map Keywords to Patterns (1–2 minutes)

Codeforces statements contain deliberate clues. Train yourself to spot them:

| Keyword in Statement | Likely Pattern |
|----------------------|----------------|
| "minimum/maximum possible", "answer is monotonic" | Binary search on answer |
| "contiguous", "subarray", "at most K" | Sliding window or prefix sums |
| "sorted array", "pair", "triplet" | Two pointers or binary search |
| "range sum", "many queries" | Prefix sums, segment tree, Fenwick |
| "range updates", "add to [L, R]" | Difference array |
| "count number of ways", "decisions at each step" | Dynamic programming |
| "cities", "roads", "connected", "shortest path" | BFS, DFS, Dijkstra, DSU |

### Step 3: Trace the Sample Manually (2 minutes)

Read the examples and compute the output by hand before coding. If your manual result matches the sample, you understood the problem. If not, reread the statement—especially the **Notes** section, which often contains critical clarifications.

### Step 4: Derive the Key Observation (5–15 minutes)

Ask yourself, in order:

1. **Can I brute-force it?** Even if too slow, a brute-force thought experiment reveals what needs optimizing.
2. **Is there a greedy choice?** Can I prove choosing the locally best option leads to a global optimum? If not provable, be cautious.
3. **What changes between adjacent states?** This often reveals prefix sums, two pointers, or DP transitions.
4. **What is the invariant?** Something that stays constant (sum, parity, XOR) often unlocks the solution.

If stuck after 15 minutes, read the editorial—but only for the idea. Then close it and implement from scratch yourself.

### Step 5: Implement, Test, Submit

Write clean code, test on the samples, then submit. If WA (Wrong Answer), test edge cases: `n=1`, all equal elements, maximum values, negative numbers (if applicable). If TLE, optimize I/O first (see Part 2).


## Part 2: Python-Specific Optimizations (Anti-TLE)

Python is slower than C++. These patterns are not optional—they are survival requirements for Codeforces.

### 2.1 Fast Input/Output (Highest Priority)

Default `input()` causes TLE on large test cases. Always use `sys.stdin`.

```python
import sys

# Basic fast input
input = sys.stdin.readline

# For maximum speed: read ALL input at once
data = sys.stdin.read().split()
ptr = 0

def next_int():
    global ptr
    val = int(data[ptr])
    ptr += 1
    return val

# Usage
n = next_int()
arr = [next_int() for _ in range(n)]
```

**Fast output**: Accumulate results in a list, join once.

```python
out = []
for i in range(n):
    out.append(str(ans))
sys.stdout.write("\n".join(out))
```

Never use `print()` in a loop for large outputs.

### 2.2 Data Structure Choices That Matter

| Use This | NOT This | Reason |
|----------|----------|--------|
| `list` as array | `dict` for dense keys | Hash lookup is slower than index access |
| `deque` for queue | `list.pop(0)` | `pop(0)` is O(n); `deque` is O(1) |
| `defaultdict(int)` | `Counter` for simple counting | Faster insertion |
| `bytearray` | `list` of booleans | Memory and speed |
| `array.array('i', ...)` | `list` of ints (fixed length) | Significant space/speed gain |

### 2.3 The Dictionary Trap (Critical for Python on CF)

**Python dictionaries can be hacked on Codeforces.** Problem setters sometimes construct inputs that cause hash collisions, making `dict` operations O(n) and triggering TLE.

**Mitigation**: If keys are integers and their exact values don't matter (only relative equality), shuffle or XOR with a random number before inserting:

```python
from random import getrandbits
RD = getrandbits(31)

# If positions matter
pos = {}
for i, x in enumerate(arr):
    pos[x ^ RD] = i
```

**Alternative**: If the range of values is small (e.g., 1 ≤ aᵢ ≤ n), use a `list` instead of a `dict` for O(1) guaranteed access.

### 2.4 Recursion Limit

Python's default recursion depth is ~1000. DFS on a tree with 10⁵ nodes will crash.

```python
import sys
sys.setrecursionlimit(10**6)
```

Better yet, implement DFS iteratively with an explicit stack to avoid recursion overhead entirely.

### 2.5 Essential Built-in Modules

```python
import bisect      # binary search on sorted lists
import math        # math.gcd(), math.isqrt()
from collections import deque, defaultdict
from heapq import heappush, heappop
```

- **Binary search**: Use `bisect.bisect_left(arr, x)` instead of writing your own loop.
- **GCD**: Use `math.gcd(a, b)`—it's implemented in C and much faster than a Python loop.


## Part 3: Pattern Recognition Decision Tree

When facing an unfamiliar problem, run through this checklist:

```
START
│
├── Is the array sorted (or can I sort it)?
│   └── YES → Two Pointers or Binary Search
│
├── Does the answer depend on a threshold? (e.g., "minimum speed", "maximum capacity")
│   └── YES → Binary Search on Answer
│
├── Are we dealing with contiguous subarrays/substrings?
│   └── YES → Sliding Window or Prefix Sums
│
├── Are there many range queries (sum, max, min)?
│   └── YES → Prefix Sums / Segment Tree / Fenwick
│
├── Is it a graph problem? (nodes, edges, connectivity)
│   └── YES → BFS (unweighted shortest path) / DFS (connectivity) / Dijkstra (weighted)
│
├── Are the same subproblems computed repeatedly?
│   └── YES → Dynamic Programming
│
├── Can I make a locally optimal choice and prove it's globally optimal?
│   └── YES → Greedy
│
└── None of the above → Try brute force first, then optimize
```

**Common mistake**: Forcing the algorithm you learned yesterday onto the problem. Let the problem guide the algorithm, not the reverse.


## Part 4: Debugging Checklist (When You Get WA or TLE)

### If Wrong Answer (WA)

1. **Edge cases**: `n=1`, empty input, all elements equal, maximum `n` with minimum values.
2. **Integer overflow**: Python handles big integers automatically, but if you're porting logic from C++, check that you're not relying on 32-bit wraparound.
3. **Off-by-one**: Check loop bounds and array indices. In Python, `range(n)` gives `0..n-1`.
4. **Floating point**: If comparing floats, use `abs(a - b) < 1e-9` instead of `==`.
5. **Copy semantics**: `b = a` for a list makes `b` reference the same list. Use `b = a.copy()` or `b = a[:]` if you need an independent copy.

### If Time Limit Exceeded (TLE)

1. **Replace `input()` with `sys.stdin.readline`** (most common fix).
2. **Replace `list.pop(0)` with `deque.popleft()`**.
3. **Replace `dict` with `list`** if keys are dense integers.
4. **Move repeated computations out of loops**.
5. **Use `sys.stdout.write` instead of `print`** for bulk output.
6. **Check for accidental O(n²)**: A nested loop over `n=10⁵` will TLE. Look for `for i in range(n): for j in range(i, n):`.
7. **Last resort**: If your algorithm is optimal but Python is too slow, consider using **PyPy** instead of CPython on Codeforces. PyPy's JIT often makes loops 3–5× faster.


## Part 5: Complete Template

```python
import sys
from collections import deque, defaultdict
from heapq import heappush, heappop
import bisect
import math

def solve():
    input = sys.stdin.readline
    
    # ---------- INPUT ----------
    n = int(input())
    arr = list(map(int, input().split()))
    
    # ---------- LOGIC ----------
    # 1. Check constraints → target complexity
    # 2. Identify pattern from keywords
    # 3. Apply the appropriate algorithm
    
    ans = 0  # placeholder
    
    # ---------- OUTPUT ----------
    sys.stdout.write(str(ans) + "\n")

if __name__ == "__main__":
    # For recursion-heavy problems:
    # sys.setrecursionlimit(10**6)
    
    # For multiple test cases:
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
```

**For problems with variable test cases**, wrap the per-test-case logic in `solve()` and call it `t` times. For single-test problems, remove the `t` loop.


## Part 6: Practice Routine That Actually Works

Based on community experience:

- **Daily**: 90–180 minutes. Pick problems where you can solve 30–40%. Sort by newest. Solve 2–4 problems.
- **Per problem**: Think seriously for 15 minutes. If no progress, read the editorial for the *idea only*, close it, and implement yourself.
- **After solving**: Write one line—"What did I learn?" This builds pattern recognition.
- **Weekly**: Join every Codeforces contest. Virtual the ones you miss.
- **Upsolve**: After each contest, solve the problems you couldn't finish during the contest.

**The 30–40% rule**: If you're solving 90% of problems, you're not learning. If you're solving 0%, you're frustrated. The sweet spot is where you struggle but succeed with effort.


## Summary: The One-Page Checklist

| Phase | Action | Time |
|-------|--------|------|
| 1 | Read constraints → target complexity | 30s |
| 2 | Scan keywords → match to pattern | 1–2 min |
| 3 | Trace sample manually | 2 min |
| 4 | Derive key observation (brute force → optimize) | 5–15 min |
| 5 | Implement with fast I/O and correct data structures | 5–20 min |
| 6 | Test edge cases → submit | 2–5 min |
| 7 | If WA: edge cases, overflow, off-by-one | — |
| 8 | If TLE: fast I/O, dict→list, PyPy | — |

**The golden rule**: Do not code until you can articulate the solution in plain English. If you can't explain it to yourself, you can't implement it correctly.
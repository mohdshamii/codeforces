# Competitive Programming Tricks & Techniques

A curated collection of practical tricks that separate fast solvers from slow ones. Organized by category.

---

## 1. Input/Output Tricks (Python)

### Read all input at once
```python
import sys
data = sys.stdin.read().split()
# Fastest for large inputs
```

### Parse multiple test cases efficiently
```python
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
```

### Output trick
```python
# Bad: print in loop (slow for large output)
# Good: accumulate and join
out = []
out.append(str(ans))
sys.stdout.write("\n".join(out))
```

### Read a grid fast
```python
grid = [input().strip() for _ in range(n)]
```

---

## 2. Array & List Tricks

### Reverse a list
```python
a[::-1]  # fast
a.reverse()  # in-place
```

### Swap without temp
```python
a, b = b, a
```

### Check if all elements satisfy condition
```python
all(x > 0 for x in arr)
any(x < 0 for x in arr)
```

### Count occurrences
```python
from collections import Counter
cnt = Counter(arr)
```

### Remove duplicates preserving order
```python
seen = set()
unique = [x for x in arr if not (x in seen or seen.add(x))]
```

### Prefix sums
```python
pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + arr[i]
# sum of arr[l:r] = pref[r] - pref[l]
```

### Difference array (range update)
```python
diff = [0] * (n + 1)
diff[l] += val
diff[r + 1] -= val
# Then prefix sum to get actual array
```

### 2D prefix sums
```python
pref = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        pref[i+1][j+1] = a[i][j] + pref[i][j+1] + pref[i+1][j] - pref[i][j]
# sum of rectangle (r1,c1) to (r2,c2):
# pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]
```

### Rotate array by k
```python
a = a[k:] + a[:k]
```

---

## 3. Binary Search Tricks

### Use bisect instead of manual binary search
```python
import bisect
bisect.bisect_left(arr, x)   # first index where arr[i] >= x
bisect.bisect_right(arr, x)  # first index where arr[i] > x
```

### Binary search on answer template
```python
def check(mid):
    # return True if mid is feasible
    pass

lo, hi = 0, 10**18
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid + 1
ans = lo
```

### Find first/last occurrence
```python
first = bisect.bisect_left(arr, x)
last = bisect.bisect_right(arr, x) - 1
```

### Integer square root (avoid float errors)
```python
import math
r = math.isqrt(n)  # exact integer sqrt
```

---

## 4. Two Pointers Tricks

### Two sum in sorted array
```python
l, r = 0, n - 1
while l < r:
    s = a[l] + a[r]
    if s == target:
        # found
        break
    elif s < target:
        l += 1
    else:
        r -= 1
```

### Sliding window (fixed size k)
```python
window_sum = sum(a[:k])
max_sum = window_sum
for i in range(k, n):
    window_sum += a[i] - a[i - k]
    max_sum = max(max_sum, window_sum)
```

### Sliding window (variable size)
```python
l = 0
for r in range(n):
    # add a[r] to window
    while window_invalid:
        # remove a[l] from window
        l += 1
    # update answer
```

---

## 5. Number Theory Tricks

### GCD/LCM
```python
import math
g = math.gcd(a, b)
lcm = a * b // g
```

### GCD of array
```python
from functools import reduce
import math
g = reduce(math.gcd, arr)
```

### Fast power (modular)
```python
def power(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result
```

### Modular inverse
```python
inv = pow(a, mod - 2, mod)  # mod must be prime
```

### Sieve of Eratosthenes
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime
```

### Count divisors
```python
def count_divisors(n):
    cnt = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            cnt += 1 if i * i == n else 2
        i += 1
    return cnt
```

### Check if perfect square
```python
r = math.isqrt(n)
is_sq = (r * r == n)
```

---

## 6. Bit Manipulation Tricks

### Check/set/clear bit
```python
x & (1 << i)        # check bit i
x | (1 << i)        # set bit i
x & ~(1 << i)       # clear bit i
x ^ (1 << i)        # toggle bit i
```

### Count set bits
```python
bin(x).count('1')
x.bit_count()  # Python 3.10+
```

### Check power of 2
```python
x > 0 and (x & (x - 1)) == 0
```

### Lowest set bit
```python
low = x & (-x)
```

### Iterate over all subsets
```python
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            # element i is in subset
```

### XOR tricks
```python
a ^ a == 0
a ^ 0 == a
# Find unique element (others appear twice)
unique = 0
for x in arr:
    unique ^= x
```

### Check if two numbers differ in exactly one bit
```python
x = a ^ b
x > 0 and (x & (x - 1)) == 0
```

---

## 7. String Tricks

### Check palindrome
```python
s == s[::-1]
```

### Count character frequency
```python
from collections import Counter
cnt = Counter(s)
```

### Convert char to int
```python
ord(c) - ord('a')  # 0-25
```

### Check anagram
```python
sorted(s1) == sorted(s2)
# or Counter(s1) == Counter(s2)
```

### Find all substrings
```python
for i in range(n):
    for j in range(i+1, n+1):
        sub = s[i:j]
```

### KMP failure function (pattern matching)
```python
def kmp_fail(p):
    fail = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = fail[j - 1]
        if p[i] == p[j]:
            j += 1
        fail[i] = j
    return fail
```

---

## 8. Graph Tricks

### BFS template
```python
from collections import deque
def bfs(start, graph):
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
```

### DFS iterative (avoid recursion limit)
```python
def dfs(start, graph):
    visited = [False] * n
    stack = [start]
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
```

### Dijkstra
```python
from heapq import heappush, heappop
def dijkstra(start, graph):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))
    return dist
```

### DSU (Union-Find)
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
```

### Topological sort (Kahn's)
```python
from collections import deque
def topo_sort(graph, indeg):
    q = deque([u for u in range(n) if indeg[u] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []  # empty if cycle
```

### Grid BFS (4 directions)
```python
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
```

### Grid BFS (8 directions)
```python
dirs = [(dx, dy) for dx in (-1,0,1) for dy in (-1,0,1) if (dx,dy) != (0,0)]
```

---

## 9. Dynamic Programming Tricks

### Memoization template
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(state):
    if base_case:
        return base_value
    return combine(dp(next_state) for ...)
```

### Knapsack (0/1)
```python
dp = [0] * (W + 1)
for w, v in items:
    for j in range(W, w - 1, -1):  # reverse!
        dp[j] = max(dp[j], dp[j - w] + v)
```

### Knapsack (unbounded)
```python
for w, v in items:
    for j in range(w, W + 1):  # forward!
        dp[j] = max(dp[j], dp[j - w] + v)
```

### LIS (O(n log n))
```python
import bisect
def lis(arr):
    tails = []
    for x in arr:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

### DP on bitmask
```python
dp = [float('inf')] * (1 << n)
dp[0] = 0
for mask in range(1 << n):
    for i in range(n):
        if not (mask & (1 << i)):
            new_mask = mask | (1 << i)
            dp[new_mask] = min(dp[new_mask], dp[mask] + cost[i])
```

---

## 10. Sorting Tricks

### Sort by custom key
```python
arr.sort(key=lambda x: (x[0], -x[1]))  # asc by first, desc by second
```

### Sort strings by length
```python
sorted(words, key=len)
```

### Sort by frequency
```python
from collections import Counter
cnt = Counter(arr)
arr.sort(key=lambda x: -cnt[x])
```

### Stable sort with index
```python
indexed = sorted(range(n), key=lambda i: arr[i])
```

### Coordinate compression
```python
sorted_unique = sorted(set(arr))
rank = {v: i for i, v in enumerate(sorted_unique)}
compressed = [rank[x] for x in arr]
```

---

## 11. Math & Formula Tricks

### Sum of 1 to n
```python
n * (n + 1) // 2
```

### Sum of squares
```python
n * (n + 1) * (2*n + 1) // 6
```

### Sum of arithmetic progression
```python
n * (first + last) // 2
```

### Number of digits
```python
len(str(n))
# or
import math
math.floor(math.log10(n)) + 1
```

### Check if integer
```python
x == int(x)
```

### Ceiling division
```python
(a + b - 1) // b
```

### Triangular number check
```python
n = int(input())
k = int((2 * n) ** 0.5)
# Check k*(k+1)//2 == n
```

### Manhattan distance
```python
abs(x1 - x2) + abs(y1 - y2)
```

### Euclidean distance
```python
math.hypot(x1 - x2, y1 - y2)
```

---

## 12. Data Structure Tricks

### Heap (min-heap)
```python
import heapq
heapq.heappush(heap, x)
heapq.heappop(heap)
heapq.heapify(arr)  # O(n)
```

### Max-heap (negate values)
```python
heapq.heappush(heap, -x)
max_val = -heapq.heappop(heap)
```

### Deque
```python
from collections import deque
d = deque()
d.appendleft(x)  # O(1)
d.popleft()      # O(1)
d.append(x)
d.pop()
```

### Ordered set (use sortedcontainers or bisect)
```python
# bisect on sorted list is O(log n) for search, O(n) for insert
import bisect
bisect.insort(arr, x)
```

### Counter most common
```python
from collections import Counter
Counter(arr).most_common(3)  # top 3
```

---

## 13. Recursion & Backtracking Tricks

### Increase recursion limit
```python
import sys
sys.setrecursionlimit(10**6)
```

### Generate all permutations
```python
from itertools import permutations
for p in permutations(arr):
    ...
```

### Generate all combinations
```python
from itertools import combinations
for c in combinations(arr, r):
    ...
```

### Cartesian product
```python
from itertools import product
for p in product([0,1], repeat=n):
    ...
```

### Backtracking template
```python
def backtrack(path, remaining):
    if not remaining:
        result.append(path[:])
        return
    for i, x in enumerate(remaining):
        path.append(x)
        backtrack(path, remaining[:i] + remaining[i+1:])
        path.pop()
```

---

## 14. Miscellaneous Tricks

### Swap two variables
```python
a, b = b, a
```

### Chained comparison
```python
if 0 <= x < n and 0 <= y < m:
    ...
```

### Ternary expression
```python
val = a if cond else b
```

### Enumerate with index
```python
for i, x in enumerate(arr):
    ...
```

### Zip arrays
```python
for a, b in zip(arr1, arr2):
    ...
```

### Flatten 2D list
```python
flat = [x for row in grid for x in row]
```

### Transpose matrix
```python
transposed = list(zip(*grid))
```

### Check if all elements equal
```python
len(set(arr)) == 1
```

### Find min/max with index
```python
min_val = min(arr)
min_idx = arr.index(min_val)
```

### Cumulative product
```python
from itertools import accumulate
import operator
list(accumulate(arr, operator.mul))
```

### Infinite generator for large sequences
```python
def gen():
    while True:
        yield something
```

### Fast string building
```python
parts = []
parts.append("x")
result = "".join(parts)
```

### Memoize with lru_cache
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

---

## 15. Common Codeforces-Specific Tricks

### Read all test cases and process
```python
import sys
data = sys.stdin.read().split()
idx = 0
t = int(data[idx]); idx += 1
for _ in range(t):
    n = int(data[idx]); idx += 1
    a = [int(data[idx + i]) for i in range(n)]
    idx += n
```

### Avoid Python dict hacking (randomize keys)
```python
from random import getrandbits
RD = getrandbits(31)
pos = {}
for i, x in enumerate(arr):
    pos[x ^ RD] = i
```

### Use PyPy on Codeforces (much faster for loops)
Just select PyPy 3 in the submission language dropdown.

### Input with multiple lines of same array
```python
arr = []
while len(arr) < n:
    arr.extend(map(int, input().split()))
```

### Print 2D grid
```python
for row in grid:
    print(''.join(row))
```

### Check if a number is representable as sum of two squares
```python
# Brute force up to sqrt
found = False
for i in range(int(math.isqrt(n)) + 1):
    if math.isqrt(n - i*i)**2 == n - i*i:
        found = True
        break
```

---

## 16. Complexity Cheat Sheet

| Operation | Python Complexity |
|-----------|-------------------|
| `list.append` | O(1) amortized |
| `list.pop()` | O(1) |
| `list.pop(0)` | O(n) ← avoid |
| `list.insert(0, x)` | O(n) ← avoid |
| `deque.appendleft` | O(1) |
| `deque.popleft` | O(1) |
| `x in list` | O(n) |
| `x in set` | O(1) avg |
| `x in dict` | O(1) avg |
| `sorted(arr)` | O(n log n) |
| `heapq.heappush` | O(log n) |
| `bisect.bisect_left` | O(log n) |
| String `+` in loop | O(n²) ← avoid |
| `''.join(parts)` | O(n) |

---

## 17. The Golden Rules

1. **Read constraints first** — they dictate the algorithm.
2. **Fast I/O always** — `sys.stdin.readline` or `sys.stdin.read().split()`.
3. **Don't use `list.pop(0)`** — use `deque`.
4. **Don't build strings with `+=` in loops** — use list + join.
5. **Increase recursion limit** for DFS/tree problems.
6. **Use `bisect`** instead of manual binary search.
7. **Shuffle dict keys** if hackable.
8. **Test edge cases**: n=1, all equal, max values.
9. **Use PyPy** on Codeforces when Python is too slow.
10. **Think before coding** — 15 minutes of thinking saves 1 hour of debugging.

---

*The best trick is knowing when to use which trick. Practice is the only way to build that intuition.*
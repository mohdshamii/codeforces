"""
Problem: 4A - Watermelon
Link: https://codeforces.com/problemset/problem/4/A
Rating: 800
Category: Math, Brute Force

Intuition:
We must divide a watermelon of weight w into two parts, each weighing an even,
positive integer (w = x + y, where x > 0, y > 0, and x % 2 == y % 2 == 0).

1. The sum of two even numbers is always even, so w must be even (w % 2 == 0).
2. The smallest possible valid split is 2 + 2 = 4.
   Therefore, w = 2 cannot be split into two positive even integers (the only
   positive split is 1 + 1, which are both odd).
3. Any even number w >= 4 can always be split as 2 + (w - 2), where both 2
   and (w - 2) are guaranteed to be positive and even.

Conclusion:
Output "YES" if w is even and w > 2; otherwise output "NO".
"""

import sys


def solve() -> None:
    w = int(sys.stdin.readline().strip())
    
    if w > 2 and w % 2 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
'''
C. K-th Not Divisible by n
time limit per test1 second
memory limit per test256 megabytes
You are given two positive integers n
 and k
. Print the k
-th positive integer that is not divisible by n
.

For example, if n=3
, and k=7
, then all numbers that are not divisible by 3
 are: 1,2,4,5,7,8,10,11,13…
. The 7
-th number among them is 10
.

Input
The first line contains an integer t
 (1≤t≤1000
) — the number of test cases in the input. Next, t
 test cases are given, one per line.

Each test case is two positive integers n
 (2≤n≤109
) and k
 (1≤k≤109
).

Output
For each test case print the k
-th positive integer that is not divisible by n
.

Example
InputCopy
6
3 7
4 12
2 1000000000
7 97
1000000000 1000000000
2 1
OutputCopy
10
15
1999999999
113
1000000001
1
'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=b//(a-1)
    d=b%(a-1)
    if d==0:
        print(c*a-1)
    else:
        print(c*a+d)
        
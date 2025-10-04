"""
Problem: Incremental Subarray
Rating: 800
Tags: math, strings
Link: https://codeforces.com/problemset/problem/2151/A
"""

import sys
input = sys.stdin.readline
def is_strictly_sorted(lst) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i+1]:
            return False
    return True
t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    b = list(map(int, input().split()))
    s = sorted(b)
    if b == [1]:
        print(n)
    elif (b == [n]) or b != s:
        print(1)
    else:
        if not is_strictly_sorted(b):
            print(1)
        else:
            print(n-(b[-1]-1))
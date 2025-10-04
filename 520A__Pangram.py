"""
Problem: Pangram
Rating: 800
Tags: implementation, strings
Link: https://codeforces.com/problemset/problem/520/A
"""

import sys
input = sys.stdin.readline
n = int(input())
z = input().strip()
s = z.lower()
a = []
for i in s:
    if i not in a:
        a.append(i)
if len(a) != 26:
    print("NO")
else:
    print("YES")
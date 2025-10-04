"""
Problem: Divisibility Problem
Rating: 800
Tags: math
Link: https://codeforces.com/problemset/problem/1328/A
"""

import math
t=int(input())
for i in range(t):
  a,b=map(int, input().split())
  c=math.ceil(a/b)
  d=(b*c)-a
  print(d)
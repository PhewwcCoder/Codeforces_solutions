"""
Problem: King Keykhosrow's Mystery
Rating: 800
Tags: brute force, chinese remainder theorem, math, number theory
Link: https://codeforces.com/problemset/problem/2034/A
"""

import math,sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print(math.lcm(a,b))
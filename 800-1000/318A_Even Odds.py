"""
Problem: Even Odds
Rating: 900
Tags: math
Link: https://codeforces.com/problemset/problem/318/A
"""

import math
n,k=map(int, input().split())
if n%2==0:
    if k<=(n/2):
            print(int(k*2-1))
    else:
            a=k-math.ceil(n/2)
            print(a*2)
else:
    if k<=math.ceil(n/2):
            print(int(k*2-1))
    else:
            a=k-math.ceil(n/2)
            print(a*2)
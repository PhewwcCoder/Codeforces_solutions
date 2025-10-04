"""
Problem: Theatre Square
Rating: 1000
Tags: math
Link: https://codeforces.com/problemset/problem/1/A
"""

import math
m,n,a=map(int, input().split())
count=math.ceil(m/a)*math.ceil(n/a)
print(count)
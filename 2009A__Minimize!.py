"""
Problem: Minimize!
Rating: 800
Tags: brute force, math
Link: https://codeforces.com/problemset/problem/2009/A
"""

t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    print(b-a)
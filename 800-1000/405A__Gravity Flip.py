"""
Problem: Gravity Flip
Rating: 900
Tags: greedy, implementation, sortings
Link: https://codeforces.com/problemset/problem/405/A
"""

n=int(input())
x=list(map(int, input().split()))
x.sort()
for i in x:
    print(i, end=" ")
"""
Problem: Ideal Generator
Rating: 800
Tags: math
Link: https://codeforces.com/problemset/problem/2093/A
"""

t= int(input())
for i in range(t):
    k=int(input())
    if k%2!=0:
        print("Yes")
    else:
        print("No")
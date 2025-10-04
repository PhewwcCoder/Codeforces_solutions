"""
Problem: Sakurako and Kosuke
Rating: 800
Tags: constructive algorithms, implementation, math
Link: https://codeforces.com/problemset/problem/2033/A
"""

t=int(input())
for i in range(t):
    n=int(input())
    if n%2==0:
        print("Sakurako")
    else:
        print("Kosuke")
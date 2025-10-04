"""
Problem: Draw a Square
Rating: 800
Tags: geometry, implementation
Link: https://codeforces.com/problemset/problem/2074/A
"""

t=int(input())
for i in range(t):
    a=input()
    l,r,d,u= map(int, a.split())
    if l==r==d==u:
      print("Yes")
    else:
       print("No")
      
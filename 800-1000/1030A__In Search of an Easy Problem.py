"""
Problem: In Search of an Easy Problem
Rating: 800
Tags: implementation
Link: https://codeforces.com/problemset/problem/1030/A
"""

n=int(input())
a=input().split()
flag=True
for i in a:
    if i=="1":
        flag=False
        break
if flag:
    print("EASY")
else:
    print("HARD")
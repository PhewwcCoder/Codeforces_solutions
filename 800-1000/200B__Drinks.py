"""
Problem: Drinks
Rating: 800
Tags: implementation, math
Link: https://codeforces.com/problemset/problem/200/B
"""

t=int(input())
o=list(map(int, input().split()))
count=0
for i in o:
    count+=i
print(count/t)
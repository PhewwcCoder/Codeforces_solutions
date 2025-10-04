"""
Problem: Vanya and Fence
Rating: 800
Tags: implementation
Link: https://codeforces.com/problemset/problem/677/A
"""

n,h=map(int, input().split())
user=list(map(int, input().split()))
count=0
for i in range(len(user)):
    if user[i]>h:
        count+=2
    else:
        count+=1
print(count)
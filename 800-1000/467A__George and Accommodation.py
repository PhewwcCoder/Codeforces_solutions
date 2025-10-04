"""
Problem: George and Accommodation
Rating: 800
Tags: implementation
Link: https://codeforces.com/problemset/problem/467/A
"""

n=int(input())
count=0
for i in range(n):
    p,q=map(int, input().split())
    sum=q-p
    if q-p>1:
        count+=1
print(count)
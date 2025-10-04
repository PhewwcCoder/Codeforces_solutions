"""
Problem: Magnets
Rating: 800
Tags: implementation
Link: https://codeforces.com/problemset/problem/344/A
"""

n=int(input())
prev=input()
count=0
for i in range(1,n):
    s=input()
    if prev[1]==s[0]:
        count+=1
    prev=s
print(count+1)
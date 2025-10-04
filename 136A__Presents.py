"""
Problem: Presents
Rating: 800
Tags: implementation
Link: https://codeforces.com/problemset/problem/136/A
"""

n=int(input())
s=list(map(int, input().split()))
d={}
output=""
for i in range(n):
    d[i+1]=s[i]
for i in range(1,n+1):
    for key,value in d.items():
        if value==i:
            output+=str(key)+" "
print(output)
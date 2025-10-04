"""
Problem: Is your horseshoe on the other hoof?
Rating: 800
Tags: implementation
Link: https://codeforces.com/problemset/problem/228/A
"""

a,b,c,d=map(int, input().split())
output=0
if a==b:
    output+=1
if a==c:
    output+=1
if a==d:
    output+=1
if a!=b and b==c:
    output+=1
if a!=b and b==d:
    output+=1
if b!=c and c==d:
    output+=1
print(output)
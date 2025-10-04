"""
Problem: Two Screens
Rating: 800
Tags: binary search, greedy, strings, two pointers
Link: https://codeforces.com/problemset/problem/2025/A
"""

q=int(input())
for i in range(q):
    s=input()
    t=input()
    count=0
    if s[0]==t[0]:
        i=0
        while i<len(s) and i<len(t) and s[i]==t[i]:
            count+=1
            i+=1
        count+=len(s)+len(t)-2*i+1
    else:
        count+=len(s)+len(t)
    print(count)
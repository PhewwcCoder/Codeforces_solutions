"""
Problem: Quintomania
Rating: 800
Tags: implementation
Link: https://codeforces.com/problemset/problem/2036/A
"""

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    flag=True
    for i in range(n-1):
        if a[i+1]-a[i]==5 or a[i+1]-a[i]==-5 or a[i+1]-a[i]==7 or a[i+1]-a[i]==-7:
            pass
        else:
            print("NO")
            flag=False
            break
    if flag:
        print("YES")
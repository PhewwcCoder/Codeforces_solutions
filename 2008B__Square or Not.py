"""
Problem: Square or Not
Rating: 800
Tags: brute force, math, strings
Link: https://codeforces.com/problemset/problem/2008/B
"""

import math
t=int(input())
for i in range(t):
    n=int(input()) #length of str
    k=input() #str
    s=int(k) #int form of str
    sqrt=math.isqrt(n)
    sq=sqrt*sqrt==n
    if sq:
        count=k.count("0")
        sqrt0=math.isqrt(count)
        sq0=sqrt0*sqrt0==count
        if count==0 and n==4:
            sq0= True
        elif count==0:
            sq0=False
        if sq0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
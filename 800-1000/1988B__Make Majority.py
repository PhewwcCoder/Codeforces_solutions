"""
Problem: Make Majority
Rating: 900
Tags: greedy, implementation
Link: https://codeforces.com/problemset/problem/1988/B
"""

user=int(input())
for i in range(user):
    user2=int(input())
    a=input()
    one=a.count("1")
    zero=a.count("0")
    throne=a.count("111")
    duo=a.count("11")
    if a[0]=="1" and a[-1]=="1":
            print("YES")
    elif len(a)>1 and a[0]=="1" and a[1]=="1":
           print("YES")
    elif len(a)>1 and a[-1]=="1" and a[-2]=="1":
           print("YES")
    elif throne>=1:
            print("YES")   
    elif duo>0 and (a[0]=="1" or a[-1]=="1"):
           print("YES")
    elif duo>=2:
            print("YES")
    else:
            print("NO")
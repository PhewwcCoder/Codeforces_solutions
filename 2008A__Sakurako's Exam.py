"""
Problem: Sakurako's Exam
Rating: 800
Tags: brute force, constructive algorithms, greedy, math
Link: https://codeforces.com/problemset/problem/2008/A
"""

t=int(input())
list1=[]
list2=[]
for i in range(t):
    a,b=map(int, input().split())
    if a%2!=0:
        print("NO")
    elif a==0 and b%2!=0:
        print("NO")
    elif a==0 and b%2==0:
        print("YES")
    elif b==0 and a%2!=0:
        print("NO")
    elif b==0 and a%2==0:
        print("YES")
    elif a%2==0 and b%2==0:
        print("YES")
    else:
        if b%2!=0:
            print("YES")
        else:
            print("NO")
"""
Problem: Hotelier
Rating: 800
Tags: brute force, data structures, implementation
Link: https://codeforces.com/problemset/problem/1200/A
"""

n=int(input())
s=input()
output=[0,0,0,0,0,0,0,0,0,0]
for i in s:
    if i=="L":
        for i in range(len(output)):
            if output[i]==0:
               output[i]=1
               break
    elif i=="R":
        for i in range(9,-1,-1):
            if output[i]==0:
                output[i]=1
                break
    else:
        output[int(i)]=0
meow=''.join(map(str,output))
print(meow)
"""
Problem: MEX rose
Rating: 900
Tags: greedy
Link: https://codeforces.com/problemset/problem/2149/C
"""

import sys
input = sys.stdin.readline
t = int(input())
for x in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    present = [False]*k
    count_k = 0
    for i in arr:
        if 0<=i<k:
            present[i] = True
        if i == k:
            count_k += 1
    missing = present.count(False)
    print(max(missing, count_k))



#Another method but less efficient CF didnt accept :'(
'''
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = set(arr)
    res = 0
    for i in range(k):
        if i not in arr2:
            res+=1
    count = arr.count(k)
    print(max(res,count)) 
'''       
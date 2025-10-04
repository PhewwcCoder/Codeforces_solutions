"""
Problem: Beautiful Year
Rating: 800
Tags: brute force
Link: https://codeforces.com/problemset/problem/271/A
"""

y=int(input())
for i in range(y,90000):
    count=""
    for _ in str(i):
        if _ not in count:
            count+=_
    if len(count)==4 and count!=str(y) :
        print(count)
        break
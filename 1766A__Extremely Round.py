"""
Problem: Extremely Round
Rating: 800
Tags: brute force, implementation
Link: https://codeforces.com/problemset/problem/1766/A
"""

for i in range(int(input())):
    n=input()
    print(int(n[0])+9*(len(n)-1))
"""
Problem: Queue at the School
Rating: 800
Tags: constructive algorithms, graph matchings, implementation, shortest paths
Link: https://codeforces.com/problemset/problem/266/B
"""

n,t=map(int, input().split())
s=input()
for i in range(t):
        n_s=s.replace("BG","GB")
        s=n_s
    
print(n_s)
"""
Problem: HQ9+
Rating: 900
Tags: implementation
Link: https://codeforces.com/problemset/problem/133/A
"""

p = input().strip()
has_output = False
for c in p:
    if c in {'H', 'Q', '9'}:
        has_output = True
        break
print("YES" if has_output else "NO")
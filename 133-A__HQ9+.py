p = input().strip()
has_output = False
for c in p:
    if c in {'H', 'Q', '9'}:
        has_output = True
        break
print("YES" if has_output else "NO")
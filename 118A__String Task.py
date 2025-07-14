s=input().lower()
output=""
for i in s:
    if i!="a" and i!="o" and i!="y" and i!="e" and i!="u" and i!="i":
        output+="."+i
print(output)
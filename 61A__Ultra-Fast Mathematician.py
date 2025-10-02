a=input()
b=input()
output=""
for i in range(len(a)):
    if a[i]!=b[i]:
        output+="1"
    else:
        output+="0"
print(output)
s=int(input())
output=""
for i in range(s):
    if i==s-1 and i%2==0:
        output+="I hate it"
        break
    if i==s-1 and i%2!=0:
        output+="I love it"
        break
    elif i%2==0:
        output+="I hate that "
    else:
        output+="I love that "
print(output)
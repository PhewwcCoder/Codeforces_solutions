s=input()
key='hello'
result=''
for i in s:
    if result=='':
        if i=='h':
            result+=i
    elif result=='h':
        if i=='e':
            result+=i
    elif result=='he':
        if i=='l':
            result+=i
    elif result=='hel':
        if i=='l':
            result+=i
    elif result=='hell':
        if i=='o':
            result+=i
if result==key:
    print("YES")
else:
    print("NO")
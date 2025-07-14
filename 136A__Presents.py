n=int(input())
s=list(map(int, input().split()))
d={}
output=""
for i in range(n):
    d[i+1]=s[i]
for i in range(1,n+1):
    for key,value in d.items():
        if value==i:
            output+=str(key)+" "
print(output)
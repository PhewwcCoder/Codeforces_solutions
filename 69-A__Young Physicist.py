n=int(input())
result=[0,0,0]
for i in range(n):
    a=list(map(int, input().split()))
    result[0]+=a[0]
    result[1]+=a[1]
    result[2]+=a[2]
if result==[0,0,0]:
    print("YES")
else:
    print("NO")
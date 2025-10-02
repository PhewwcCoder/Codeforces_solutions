t=int(input())
for _ in range(t):
    n,n2=map(int, input().split())
    l=input().split()
    k=list(map(int,l))
    k.sort()
    count=0
    for i in range(len(k)-1):
        if k[i]==1:
            count+=1
        else:
            count+=k[i]-1+k[i]           
    print(count)
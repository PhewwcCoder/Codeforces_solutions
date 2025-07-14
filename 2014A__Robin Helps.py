t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    value=list(map(int,input().split()))
    money=0
    help=0
    for i in range(n):
        if value[i]!=0 and value[i]>=k:
            money+=value[i]
        elif value[i]==0 and money>0:
            help+=1
            money-=1
    print(help)
t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    count=0
    if k!=1:
        while n>0:
            count+=n%k
            n//=k
        print(count)
    else:
        print(n)
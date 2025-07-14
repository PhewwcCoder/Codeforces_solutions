n=int(input())#number of coins
a=list(map(int, input().split()))
a.sort()
a.reverse()
me=0
count=0
for i in a:
    count+=i
twin=count    
for i in range(len(a)):
    me+=a[i]
    twin-=a[i]
    if me>twin:
        print(i+1)
        break
t=int(input())
for i in range(t):
    z=list(map(int,input().split()))
    z.sort()
    z.reverse()
    a,b,c=[z[0],z[1],z[2]]
    count=0
    if a%2!=0 and b%2!=0 and c%2!=0:
        print("-1")
    elif b==0 and c==0:
        if a%2==0:
            print(0)
        else:
            print(-1)
    elif c==0 and a>b and (a-b)%2!=0:
        print(-1)
    elif b==c and a>b and a%2!=0:
        print(-1)
    elif a==b and a>c and c%2!=0:
            print(-1)
    elif (a%2==0 and b%2==0 and c%2!=0) or (a%2==0 and b%2!=0 and c%2==0) or (a%2!=0 and b%2==0 and c%2==0):
        print(-1)
    else:
        for i in range(a+b+c):
            if not z[0]==z[1]==z[2] and z[1]!=0 :
                z[0]-=1
                z[1]-=1
                count+=1
                z.sort()
                z.reverse()
            else:
                if z[0]%2!=0 and z[1]%2!=0 and z[2]%2!=0:
                    print("-1")
                    break
                elif z[1]==0:
                    print(count)
                    break
                else:
                    count+=(3*z[0])/2
                    print(int(count))
                    break
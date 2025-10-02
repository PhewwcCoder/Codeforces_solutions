t=int(input())
list1=[]
list2=[]
for i in range(t):
    a,b=map(int, input().split())
    if a%2!=0:
        print("NO")
    elif a==0 and b%2!=0:
        print("NO")
    elif a==0 and b%2==0:
        print("YES")
    elif b==0 and a%2!=0:
        print("NO")
    elif b==0 and a%2==0:
        print("YES")
    elif a%2==0 and b%2==0:
        print("YES")
    else:
        if b%2!=0:
            print("YES")
        else:
            print("NO")
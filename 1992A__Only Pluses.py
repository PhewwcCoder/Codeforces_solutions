t=int(input())
for i in range(t):
    a,b,c=map(int, input().split())
    for i in range(5):
        if a<b and a<c:
            a+=1
        elif b<a and b<c:
            b+=1
        elif c<b and c<a:
            c+=1
        elif a==b and a<c:
            a+=1
        elif a==b and a==c:
            a+=1
        elif b==c and b<a:
            b+=1
        elif a==c and a<b:
            a+=1
    print(a*b*c)
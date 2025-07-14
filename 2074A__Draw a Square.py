t=int(input())
for i in range(t):
    a=input()
    l,r,d,u= map(int, a.split())
    if l==r==d==u:
      print("Yes")
    else:
       print("No")
      
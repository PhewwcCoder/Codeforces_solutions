a=int(input())
b=int(input())
c=int(input())
sum=0
list1=[a,b,c]
if 1 not in list1:
    sum+=(a*b*c)
elif list1.count(1)==3:
    sum=3
elif list1.count(1)==1:
    if a==1:
        sum=(a+b)*c
    if b==1:
        if a>c:
            sum=(b+c)*a
        else:
            sum=(a+b)*c
    if c==1:
        sum=a*(b+c)
else:
    if a==b==1:
        sum=(a+b)*c
    if b==c==1:
        sum=(b+c)*a
    if a==c==1:
        sum=a+b+c
print(sum)
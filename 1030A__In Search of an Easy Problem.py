n=int(input())
a=input().split()
flag=True
for i in a:
    if i=="1":
        flag=False
        break
if flag:
    print("EASY")
else:
    print("HARD")
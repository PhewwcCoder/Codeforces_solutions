n=int(input())
prev=input()
count=0
for i in range(1,n):
    s=input()
    if prev[1]==s[0]:
        count+=1
    prev=s
print(count+1)
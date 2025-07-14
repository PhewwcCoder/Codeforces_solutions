t=int(input())
o=list(map(int, input().split()))
count=0
for i in o:
    count+=i
print(count/t)
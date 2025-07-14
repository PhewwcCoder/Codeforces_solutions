t=int(input())
for i in range(t):
    n= int(input())
    a=list(map(int, input().split()))
    found= False
    ht={0:3, 1:1, 3:1, 2:2, 5:1}
    ht2={0:0, 1:0, 3:0, 2:0, 5:0}
    count=0
    for i in a:
        if ht == ht2:
            print(count)
            found= True
            break
        else:
            if i in ht:
                if ht[i]!=ht2[i]:
                    ht[i]-=1
        count+=1
    if found == False:
        if ht == ht2:
            print(count)
        else:
            print(0)
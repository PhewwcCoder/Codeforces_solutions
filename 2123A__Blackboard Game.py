t = int(input())
for i in range(t):
    n = int(input())
    counter = [0,0,0,0]
    j = 0
    for i in range(n):
        if j == 4:
            j = 0
        if j == 0:
            counter[j]+=1
        elif j == 1:
            counter[j]+=1
        elif j == 2:
            counter[j]+=1
        elif j == 3:
            counter[j]+=1
        j+=1
    if counter[0] == counter[3] and counter[1] == counter[2]:
        print('Bob')
    else:
        print('Alice')
#idea
# 0=4 as a+b = 3(mod4)
#0,1,2,3..0,1,2,3..and so on the pattern
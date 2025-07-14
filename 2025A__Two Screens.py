q=int(input())
for i in range(q):
    s=input()
    t=input()
    count=0
    if s[0]==t[0]:
        i=0
        while i<len(s) and i<len(t) and s[i]==t[i]:
            count+=1
            i+=1
        count+=len(s)+len(t)-2*i+1
    else:
        count+=len(s)+len(t)
    print(count)
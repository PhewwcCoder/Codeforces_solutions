t=int(input())
for i in range(t):
    n=int(input())
    output=[]
    for i in range(n):
        s=input()       
        for i in range(len(s)):
            if s[i]=="#":
                output.append(i+1)
    output3=output[::-1]            
    output2=" ".join(map(str,output3))
    
    print(output2)
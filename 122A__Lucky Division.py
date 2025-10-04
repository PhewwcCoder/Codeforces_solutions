"""
Problem: Lucky Division
Rating: 1000
Tags: brute force, number theory
Link: https://codeforces.com/problemset/problem/122/A
"""

def lucky(n):
    str_n=str(n)
    count=0
    for i in str_n:
        if (i=="4" or i=="7") and count==len(str_n)-1:
            return True
        if (i=="4" or i=="7"):
            count+=1
        else:
            break
        
    divisor=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisor.append(i)
            if i!=n//i:
                divisor.append(n//i)
    for j in divisor:
        str_n=str(j)
        count=0
        for i in str_n:
            if (i=="4" or i=="7") and count==len(str_n)-1:
                return True
            if (i=="4" or i=="7"):
                count+=1
            else:
                break
    return False
n=int(input())
if lucky(n):
    print("YES")
else:
    print("NO")
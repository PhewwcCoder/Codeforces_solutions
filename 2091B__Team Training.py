t=int(input())
for i in range(t):
    n,x= map(int, input().split())
    a=list(map(int, input().split()))
    stack=sorted(a)
    restack=[]
    count=0
    while stack:
        if stack[-1]>=x:
            stack.pop()
            count+=1
        else:
            restack.append(stack.pop())
            result= len(restack)*min(restack)
            if result>=x:
                count+=1
                result=0
                restack=[]
    print(count)
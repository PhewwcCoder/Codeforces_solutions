import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    arr = [0]*(2*n)
    arr[0],arr[n] = n,n
    for i in range(1,n):
        arr[i] = n-i
    k = 1
    for j in range(n+1,2*n):
        arr[j] = k
        k+=1
    print(*arr)

#Idea:

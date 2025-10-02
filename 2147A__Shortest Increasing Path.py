import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if x<y:
        print(2)
    elif x == y:
        print(-1)
    else:
        if 1 < y < x-1 :
            print(3)
        else:
            print(-1)
    


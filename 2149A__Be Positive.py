import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    minus1 = arr.count(-1)
    zero = arr.count(0)
    result = zero
    if minus1%2 != 0 :
        print(result+2)
    else:
        print(result)
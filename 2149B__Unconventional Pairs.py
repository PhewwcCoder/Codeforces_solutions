import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr1 = []
    arr2 = []
    diff = []
    for i in range(n):
        if i%2 == 0:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    for i in range(len(arr1)):
        diff.append(abs(arr1[i]-arr2[i]))
    print(max(diff))


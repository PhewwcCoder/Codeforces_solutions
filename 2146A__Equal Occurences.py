import sys,operator
from collections import Counter
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = dict(Counter(arr))
    res = dict(sorted(count.items(), key = operator.itemgetter(1)))
    k = len(res)
    output = 0
    for key in res:
        result = res[key]*k
        k-=1
        if result > output:
            output = result
    print(output)


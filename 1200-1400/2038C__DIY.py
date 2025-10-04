"""
Problem: DIY
Rating: 1400
Tags: data structures, geometry, greedy, sortings
Link: https://codeforces.com/problemset/problem/2038/C
"""

def solve():
    a = int(input())
    ques = list(map(int, input().split()))
    usable = []
    freq = {}
    for i in ques:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    for num,count in freq.items():
        if count >= 2:
            for i in range(count//2):
                usable.append(num)
    if len(usable) < 4:
        print("NO")
        return
    usable.sort()
    x1 = usable[0]
    y1 = usable[1]
    if (usable[-2]-usable[0])*(usable[-1]-usable[1]) > (usable[-1]-usable[0])*(usable[-2]-usable[1]):
        x2 = usable[-2]
        y2 = usable[-1]
    else:
        x2 = usable[-1]
        y2 = usable[-2]
    print("YES")
    print(x1,y1,x2,y1,x2,y2,x1,y2)
t = int(input())
for i in range(t):
    solve()
import math
t=int(input())
for i in range(t):
  a,b=map(int, input().split())
  c=math.ceil(a/b)
  d=(b*c)-a
  print(d)
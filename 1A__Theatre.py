import math
m,n,a=map(int, input().split())
count=math.ceil(m/a)*math.ceil(n/a)
print(count)
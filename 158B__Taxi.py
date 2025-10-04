"""
Problem: Taxi
Rating: 1100
Tags: *special, greedy, implementation
Link: https://codeforces.com/problemset/problem/158/B
"""

n= int(input())
s=list(map(int, input().split()))
count1=0
count2=0
count3=0
count4=0
for i in s:
    if i==1:
        count1+=1
    elif i==2:
        count2+=1
    elif i==3:
        count3+=1
    elif i==4:
        count4+=1
taxi=count4
min_31= min(count1,count3)
taxi+=min_31
taxi+=(count3-min_31)
count1-= min_31
taxi+=count2//2
if count2%2!=0:
    taxi+=1
    count1= max(0,count1-2)
taxi+=count1//4
if count1%4!=0:
    taxi+=1
print(taxi)
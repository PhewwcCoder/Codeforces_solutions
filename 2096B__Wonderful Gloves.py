t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    hashmap = {}
    sum = 1
    min_sum = []
    for i in range(n):
        hashmap[i] = [arr1[i],arr2[i]]
    for i in hashmap:
        sum+=max(hashmap[i])
        min_sum.append(min(hashmap[i]))
    min_sum.sort(reverse=True)
    for i in range(k-1):
        sum+=min_sum[i]
    print(sum)

#idea
#hashmap index and an array to calculate and store the min val
#sum e hashmap theke every max nisi (pore +1 na kore shurutei sum=1)
#sort kore reverse and taking k-1 from min_array

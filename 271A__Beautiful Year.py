y=int(input())
for i in range(y,90000):
    count=""
    for _ in str(i):
        if _ not in count:
            count+=_
    if len(count)==4 and count!=str(y) :
        print(count)
        break
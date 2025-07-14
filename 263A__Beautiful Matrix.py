matrix=[]
for i in range(5):
    matrix.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            row,col=i,j
sum=abs(2-row)+abs(2-col)
print(sum)
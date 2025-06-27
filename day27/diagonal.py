mat1 = [[1,2,3,4] ,[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat2 = [[1,1,1,1] , [0,0,0,0], [0,0,0,1]]
result=0
row=4
col=4
mat=[]
for i in range(0, row):
    rowList = []
    for j in range(0 , col):
        rowList.append(mat1[i][j] + mat2[i][j])
    result.append(rowList)
for i in range(row):
    for j in range(col):
        if i == j or i + j == row - 1:
            result += mat[i][j]
print(result)
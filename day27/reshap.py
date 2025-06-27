mat=[[1,2],[3,4]]
r=1
c=4
list= []
for row in mat:
    list.extend(row)
    if len(list) != r * c:
        print(mat)
    result = []
    for i in range(r):
        result.append(list[i * c:(i + 1) * c])
    print(result)

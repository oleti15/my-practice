matrix=[[1,2,3],[1,0,2],[2,3,4]]
rows = len(matrix)
cols = len(matrix[0])
rowZero = False
colZero = False

    # Check if first row has a zero
for j in range(cols):
    if matrix[0][j] == 0:
        rowZero = True

    # Check if first column has a zero
for i in range(rows):
    if matrix[i][0] == 0:
        colZero = True

    # Use first row and column to mark other rows and columns
for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0

    # Set zeroes based on markers
for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0

    # Zero out the first row if needed
if rowZero:
    for j in range(cols):
        matrix[0][j] = 0

    # Zero out the first column if needed
if colZero:
    for i in range(rows):
        matrix[i][0] = 0
print(matrix)
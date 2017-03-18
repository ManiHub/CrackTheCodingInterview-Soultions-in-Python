# Replace corresponding row and column with zero for a zero element in Matrix

def Zero(matrix):
    rows = []
    cols = []

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j]==0:
                rows.append(i)
                cols.append(j)

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j]=0

    return matrix

#matrix
arr = [[1,0,1],[1,1,1],[1,1,1]]
print(Zero(arr))


  



def matrix_array(n,m):
    matrix=[0]*m
    print matrix

    for i in range(len(matrix)):
        matrix[i]=[0]*n
    return matrix

print(matrix_array(2,3))

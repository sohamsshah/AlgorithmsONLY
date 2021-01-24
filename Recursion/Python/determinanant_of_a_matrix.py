#User function Template for python3

def computeMatrix(X,N):
    main = [] #matrix of [[[4,6], [4,9]], [[4,6], [4,9]],[[4,6], [4,9]]] 
    for k in range(N):
        row_temp = [] #matrix of [[4,6], [4,9]]
        for i in range(1,N):
            col_temp = []
            for j in range(N):
                if j != k:
                    col_temp.append(X[i][j])
            row_temp.append(col_temp)
        main.append(row_temp)
    return main
    

def determinantOfMatrix(matrix,n):
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) 
    det_matrix = computeMatrix(matrix,n)
    ans = 0
    for i in range(len(det_matrix)):
        ans+=(((-1)**i)*determinantOfMatrix(det_matrix[i],n-1)*matrix[0][i])
    return ans
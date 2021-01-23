#User function Template for python3
n1,m1 = input().split()
n2,m2 = input().split()

def sumMatrix(A,B):
    if n1 != n2 or m1 != m2:
        return [[-1]]
    res = [[0 for i in range(m1)] for i in range(n1)]
    for i in range(n1):
        for j in range(m1):
            res[i][j] = A[i][j] + B[i][j]
    return res
#User function Template for python3
def transpose(X):
    n = len(X)
    m = 0
    for i in range(n):
        for j in range(m,len(X)):
            if i != j:
                X[i][j],X[j][i] = X[j][i],X[i][j]
        m+=1
    return X
        
        
def rotateby90(a, n):
    for i in range(len(a)):
        a[i] = a[i][::-1]
    transpose(a)
def convertToWave(A,N):
    #Your code here
    for i in range(0,N,2):
        if i>= len(A)-1:
            break
        A[i], A[i+1] = A[i+1], A[i]
def equilibriumPoint(A, N):
    # Your code here
    total = sum(A)
    left_sum = 0
    if len(A) == 1:
        return 1
    for i in range(N):
        if left_sum == (total-left_sum-A[i]):
            return i+1
        left_sum+=A[i]
    return -1
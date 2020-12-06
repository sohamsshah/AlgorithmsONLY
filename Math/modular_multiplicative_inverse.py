def modInverse(a,m):
    ##Your code here
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return -1
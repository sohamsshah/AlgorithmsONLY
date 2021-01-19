def printIntersection(a, b, n, m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: array of intersection of two array or -1
    '''
    # code here
    lis = []
    N_pointer = 0
    M_pointer = 0
    while N_pointer<n and M_pointer<m:
        if b[M_pointer] == a[N_pointer]:
            if len(lis) == 0:
                lis.append(b[M_pointer])
            else:
                if lis[-1] != b[M_pointer]:
                    lis.append(b[M_pointer])
            N_pointer+=1
            M_pointer+=1
        elif b[M_pointer] < a[N_pointer]:
            M_pointer+=1
        elif b[M_pointer] > a[N_pointer]:
            N_pointer+=1
        
    return lis


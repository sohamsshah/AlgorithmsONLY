def leaders(A,N):
    #Your code here
    leaders = []
    r_maximum = -99999999
    for i in range(N-1, -1, -1):
        if r_maximum <= A[i]:
            r_maximum = A[i]
            leaders.append(r_maximum)
    return leaders[::-1]
            
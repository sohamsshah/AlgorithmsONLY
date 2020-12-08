def trappingWater(arr,n):
    prefix_left, prefix_right = [],[]
    l_max, r_max = -999999, -999999
    total= 0
    for i in range(n):
        l_max = max(l_max,arr[i])
        prefix_left.append(l_max)
    for i in range(n-1, -1, -1):
        r_max = max(r_max, arr[i])
        prefix_right.append(r_max)
    prefix_right = prefix_right[::-1]
    
    for i in range(1,n-1):
        total+=(min(prefix_left[i], prefix_right[i]) - arr[i])
        
    return total
        
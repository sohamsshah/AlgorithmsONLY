def firstRepeated(arr, n):
    
    #arr : given array
    #n : size of the array
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = i+1
        else:
            return dic[arr[i]]
    return -1
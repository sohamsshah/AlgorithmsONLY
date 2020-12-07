def immediateSmaller(arr,n,x):
    #return required ans
    
    #code here
    diff = 9999999
    for i in arr:
        if x > i:
            diff = min(diff,x-i)
    if diff != 9999999:
        return x-diff
    return -1
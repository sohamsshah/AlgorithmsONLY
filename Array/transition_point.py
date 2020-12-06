def transitionPoint(arr, n):
    #Code here
    start = 0
    end = len(arr) - 1
    if len(arr)==1:
        if arr[0] == 0:
            return -1
        else:
            return 0
    while start<=end:
        mid = (start+end) // 2
        if arr[mid] == 0:         
            start = mid+1
        elif arr[mid] == 1:
            if mid == 0 or (mid >0  and arr[mid-1] == 0):
                return mid
            end = mid-1
    return -1
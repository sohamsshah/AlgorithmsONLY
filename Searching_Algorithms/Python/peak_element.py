def peakElement(arr, n):
    l = 0
    r = n-1
    if n==1:
        return 0
    while l<=r:
        mid = (l+r)//2
        if mid > 0 and mid < n-1:
            if arr[mid] >= arr[mid+1] and arr[mid] >= arr[mid-1]:
                return mid
            elif arr[mid+1] > arr[mid]:
                l = mid+1
            else:
                r = mid-1
        else:
            if mid == 0:
                if arr[0] >= arr[1]:
                    return 0
                else:
                    return 1
            elif mid == n-1:
                if arr[n-1] >= arr[n-2]:
                    return n-1
                else:
                    return n-2
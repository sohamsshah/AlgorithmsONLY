def search(arr,n,k):
    l = 0
    r = n-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == k:
            return mid
        if mid>=l and arr[mid-1] == k:
            return mid-1
        if mid <=r and arr[mid+1] ==k:
            return mid+1
        if mid > k:
            r = mid-2
        elif mid < k:
            l = mid+2
    return -1
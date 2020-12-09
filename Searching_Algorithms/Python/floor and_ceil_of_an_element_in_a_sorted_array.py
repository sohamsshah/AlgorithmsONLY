def floor(arr,n,k):
    l = 0
    r = n-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == k:
            return arr[mid]
        if arr[mid] < k:
            res = arr[mid]
            l = mid+1
        if arr[mid] > k:
            r = mid-1
    return res

def ceil(arr,n,k):
    l = 0
    r = n-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==k:
            return arr[mid]
        if arr[mid]>k:
            res = arr[mid]
            r = mid-1
        elif arr[mid]<k:
            l = mid+1
    return res
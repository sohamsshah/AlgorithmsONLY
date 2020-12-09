def binarySearch(arr,n,k):
    l = 0
    r = n-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == k:
            return [arr[mid]]
        if k < arr[mid]:
            r = mid-1
        if k > arr[mid]:
            l = mid+1
    return [l,r]

def minimumDifference(arr,n,k):
    res = binarySearch(arr,n,k)
    if len(res) == 0:
        return 0
    else:
        return min(res[0]-k, res[1]-k)


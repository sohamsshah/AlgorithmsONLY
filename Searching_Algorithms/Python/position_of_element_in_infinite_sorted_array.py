def binarySearch(arr, l,r, n, k):
    while l<=r:
        mid=(l+r)//2
        if arr[mid] ==k:
            return mid
        if arr[mid] > k:
            r = mid-1
        elif arr[mid] < k:
            l = mid+1
    return -1

def infiniteSearch(arr,n,k):
    l = 0
    r = 1
    while k > arr[r]:
        l = r
        r*=2
    binarySearch(arr,l,r,n,k)
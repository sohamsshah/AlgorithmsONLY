def nextAlphabeticalLetter(arr,n,k):
    l = 0
    r = n-1
    res=arr[0]
    while l<=r:
        mid=(l+r)//2
        if arr[mid] == k:
            l = mid+1
        if arr[mid]>k:
            res =arr[mid]
            r = mid-1
        if arr[mid]<k:
            l = mid+1
    return res
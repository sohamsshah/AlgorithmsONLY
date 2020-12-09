def binarysearch(arr, l, r , k):
	while l <= r:
	    mid = (l+r)//2
	    if arr[mid] == k:
	        return mid
	    if arr[mid] < k:
	        l = mid+1
	    elif arr[mid] > k:
	        r = mid-1
    return -1

def findmin(arr,n):
    l = 0
    r = n-1
    if arr[0] <= arr[n-1]:
        return binarysearch(arr, l, r, k)
    while l <= r:
        mid = (l+r)//2
        nxt = (mid+1)%n
        prev = (mid+n-1)%n
        if arr[prev] >= arr[mid]:
            return mid
        if arr[nxt] <= arr[mid]:
            return mid+1
        if arr[mid] >= arr[l]:
            l = mid+1
        elif arr[mid] <= arr[r]:
            r = mid-1
    

def Search(arr,n,k):
    index = findmin(arr,n)
    x = binarysearch(arr,0, index-1,k)
    y = binarysearch(arr, index, n-1,k)
    if x == -1 and y == -1:
        return -1
    if x != -1:
        return x
    else:
        return y
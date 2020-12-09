class Solution:	
	def binarysearch(self, arr, n, k):
		l = 0
		r = n-1
		while l <= r:
		    mid = l + ( r-l // 2 )
		    if arr[mid] == k:
		        return mid
		    if arr[mid] < k:
		        l = mid+1
		    elif arr[mid] > k:
		        r = mid-1
	    return -1
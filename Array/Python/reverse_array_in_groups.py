class Solution:	
	def reverseInGroups(self, arr, N, K):
		# code here
        for i in range(0,N,K):
            start,end = i,i+K-1
            if end>len(arr)-1:
                end = len(arr)-1
            while start<=end:
                arr[start],arr[end] = arr[end], arr[start]
                start+=1
                end-=1
            
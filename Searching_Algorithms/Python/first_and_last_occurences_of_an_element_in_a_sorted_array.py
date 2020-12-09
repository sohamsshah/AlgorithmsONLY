class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        def searchOccurence(arr,target,order):
            n = len(arr)
            l = 0
            r = n-1
            res = -1
            while l<=r:
                mid= (l+r)//2
                if order == -1:
                    if arr[mid]==target:
                        res = mid
                        r = mid-1
                    if arr[mid] > target:
                        r = mid-1
                    elif arr[mid] < target:
                        l = mid+1
                elif order == 1:
                    if arr[mid]== target:
                        res = mid
                        l = mid+1
                    if arr[mid] > target:
                        r = mid-1
                    elif arr[mid] < target:
                        l = mid+1            
                    
            return res
        
        
        return [searchOccurence(arr,target,-1), searchOccurence(arr,target,1)]
        
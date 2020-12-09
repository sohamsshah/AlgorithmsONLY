class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        if nums[0] <= nums[n-1]:
            return nums[0]
        while l<=r:
            mid = (l+r)//2
            nxt = (mid+1)%n
            prev = (mid+n-1)%n
            if nums[mid]<=nums[prev]:
                return nums[mid]
            if nums[mid]>= nums[nxt]:
                return nums[mid+1]
            if nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid - 1
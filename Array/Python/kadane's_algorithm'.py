def maxSubArraySum(nums,size):
    ##Your code here
    sum = 0
    maxi = -999999
    for i in range(size):
        sum+=nums[i]
        maxi = max(maxi, sum)
        if sum<0:
            sum=0
    return maxi
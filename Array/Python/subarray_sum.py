def subArraySum(arr, n, sum): 

    low = 0 
    high = 0
    curr_sum = arr[low]
    
    while low <= high and high <= n - 1:
        if curr_sum == sum:
            print(low,high)
        elif curr_sum < sum:
            high = high + 1
            curr_sum = curr_sum + arr[high]
        else:
            curr_sum = curr_sum - arr[low]
            
    print(-1)
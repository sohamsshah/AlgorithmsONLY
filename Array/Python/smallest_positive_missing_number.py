def findMissing(nums, size): 
    for i in range(size):
        correctPos = nums[i]-1 # number 3 goes to index 2
        while 1 <= nums[i] <= size and nums[i] != nums[correctPos]:
            nums[i], nums[correctPos] = nums[correctPos], nums[i]
            correctPos = nums[i]-1 # now nums[i] has changed
    for i in range(size):
        if i+1 != nums[i]:
            return i+1
    return size+1
            
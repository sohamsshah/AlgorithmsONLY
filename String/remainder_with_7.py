#your task is to complete this function
#Function should return the required answer
#You are not allowed to convert string to integer
def remainderWith7(string):
    series = [1,3,2,-1,-3,-2]
    ans = 0
    ind = 0
    for i in string[::-1]:
        ans+=(series[ind]*int(i))
        ans%=7
        ind = (ind + 1) % 6
    if ans < 0:
        ans = (ans+7)%7
    return ans
        
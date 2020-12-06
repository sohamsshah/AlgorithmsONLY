import math
def digitsInFactorial(N):
    ans = 0
    for i in range(1,N+1):
        ans+=(math.log(i,10))
    
    return math.floor(ans+1)
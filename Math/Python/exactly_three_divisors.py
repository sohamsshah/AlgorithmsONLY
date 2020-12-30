import math
def exactly3Divisors(N):
    # code here
    def isPrime(N):
        # code here
        for i in range(2, math.ceil(math.sqrt(N))):
            if N%i == 0:
                return False
        return True
    def isPerfectSquare(x): 
  
        # Find floating point value of  
        # square root of x. 
        sr = math.sqrt(x) 
       
        # If square root is an integer 
        return ((sr - math.floor(sr)) == 0) 
        
    cnt=0
    for i in range(2, N+1):
        if isPerfectSquare(i) == True:
            if isPrime(i) == True:
                cnt+=1
    return cnt


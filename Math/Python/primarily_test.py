import math
def isPrime(N):
    # code here
    for i in range(2, math.ceil(math.sqrt(N))+1):
        if N%i == 0:
            return False
    return True
class Solution:
    def getSmallestDivNum(self, n): 
        # code here
        def gcd(a,b):
            if a==0:
                return b
            return gcd(b%a,a)
        ans = 1
        for i in range(1,n+1):
            ans = int((ans*i)/gcd(ans,i))
        return ans
            


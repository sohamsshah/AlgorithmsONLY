import math
class Solution:
	def quadraticRoots(self, a, b, c):
        # code here
        if b**2 - 4*a*c < 0:
            return [-1]
        
        lis = [math.floor((-b + math.sqrt(b**2 - 4*a*c) )/ (2*a)), math.floor((-b - math.sqrt(b**2 - 4*a*c) )/ (2*a))]
        return sorted(lis, reverse=True)
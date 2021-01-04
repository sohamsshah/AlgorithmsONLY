# To just check if it can measure the water by the jugs or not

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(x,y):
            if x==0: return y
            else: return gcd(y%x,x)
        if z==0: return True
        if z>x+y: return False
        g = gcd(x,y)
        if z%g==0: return True
        return False

# Brute Force DFS to find all the cases that make up the required volume

class Solution2:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        seen = set()   
        res = False
        def dfs(a, b):
            global res
            if res:
                return
            elif (a,b) in seen:
                return 
            seen.add((a,b))
            if a == z or b == z:
                res = True
                return 
            ## Recursive Cases:
            dfs(0, b)
            dfs(a, 0)
            dfs(x, b)
            dfs(a, y)
            ## b pour into a:
            amount = min(b, x-a)
            dfs(a+amount, b-amount)
            ## a pour into b:
            amount = min(a, y-b)
            dfs(a-amount, b+amount)
        dfs(0, 0)





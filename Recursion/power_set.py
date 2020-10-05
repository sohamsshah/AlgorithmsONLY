# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:51:50 2020

@author: Soham Shah
"""

arr = [1,2,3,4]
ans = []
def solve(input, output):
    if len(input) == 0:
        ans.append(output)
        return
    output1 = output.copy()
    output2 = output.copy()
    output1.append(input[0])
    input = input[1:]
    print(output1, output2, input)
    solve(input, output1)
    solve(input, output2)
    
solve(arr, [])

print(ans)
    
    
        
    
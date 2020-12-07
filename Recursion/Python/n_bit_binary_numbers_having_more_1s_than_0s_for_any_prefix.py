# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:10:35 2020

@author: Soham Shah
"""

n = 3
ans = []
def solve(one, zero, n, output):
    if n == 0:
        ans.append(output)
        return
    output1 = output[:]
    output1+='1'
    solve(one+1, zero, n-1, output1)
    if one > zero:
        output2 = output[:]
        output2+='0'
        solve(one, zero+1,n-1, output2)
        
solve(0,0,n,"")
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 00:16:27 2020

@author: Soham Shah
"""

# Balanced Parantheses

n = 3
ans = []

def solve(open, close, output):
    if open == 0 and close == 0:
        ans.append(output)
    if open != 0:
        output1 = output[:]
        output1+=('(')
        solve(open-1, close, output1)
    if close > open:
        output2 = output[:]
        output2+=(')')
        solve(open, close-1, output2)
        
solve(n,n,"")
    
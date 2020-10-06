# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:27:21 2020

@author: Soham Shah
"""

arr = ['A', 'B', 'C']
k = 2

def solve(arr, k, index, ans):
    if len(arr) == 1:
        ans = arr[0]
        return
    index = (index+k)%(len(arr))
    arr.pop(index)
    print(arr)
    solve(arr, k, index, ans)
    
solve(arr, k, 0, -1)
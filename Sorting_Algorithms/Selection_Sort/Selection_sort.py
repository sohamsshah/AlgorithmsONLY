# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:48:59 2020

@author: Soham Shah
"""

# Selection Sort


# Approach 1
arr = [64 ,25 ,12 ,22 ,11]
ans = []
for i in range(len(arr)):
    ind = arr.index(min(arr))
    ans.append(min(arr))
    arr.remove(arr[ind])

# Approach 2
    
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index] , arr[i]
    
    
    
    
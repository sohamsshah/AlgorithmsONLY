# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:32:44 2020

@author: Soham Shah
"""

# Insertion Sort - Iterative (Approach 1)

arr = [12, 11, 13, 5, 6]

for i in range(1,len(arr)):
    for j in range(0,i):
        if arr[i] < arr[j]:
            arr[j], arr[i] = arr[i], arr[j]

# Insertion Sort - Iterative (Approach 2)

for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >= 0 and key < arr[j] : 
            arr[j + 1] = arr[j] 
            j -= 1
    arr[j + 1] = key 
    
# Insertion sort - Recursive

def insertionSortRecursive(arr,n): 
    
    if n<=1: 
        return
    insertionSortRecursive(arr,n-1) 
    last = arr[n-1] 
    j = n-2  
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j] 
        j = j-1
  
    arr[j+1]=last 
        
print(insertionSortRecursive(arr))
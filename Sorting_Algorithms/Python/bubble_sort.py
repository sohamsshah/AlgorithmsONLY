# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:08:23 2020

@author: Soham Shah
"""

# Bubble Sort - Iterative

arr = [64, 34, 25, 12, 22, 11, 90] 

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            
# Bubble Sort - Optimized

for i in range(len(arr)-1):
    swapped = False
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            swapped = True
    if swapped == False:
        break

# Bubble Sort Recursive
        
def bubble_sort(listt): 
    for i, num in enumerate(listt): 
        try: 
            if listt[i+1] < num: 
                listt[i] = listt[i+1] 
                listt[i+1] = num 
                bubble_sort(listt) 
        except IndexError: 
            pass
    return listt 
  
bubble_sort(arr)

  
        
            
            

    
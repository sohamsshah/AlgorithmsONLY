# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:32:23 2020

@author: Soham Shah
"""

def Counting_Sort(arr):
    dict ={}
    
    for i in range(max(arr)+1):
        dict[i] = 0
    
    for i in arr:
        dict[i]+=1
    
    for i in range(1,len(dict)):
        dict[i] = dict[i] + dict[i-1]
        
    ans = [0 for i in range(max(dict.values())+1)]
    
    for i in arr:
        ans[dict[i]] = i
        dict[i]-=1

    return ans[1:]  


# Counting Sort - Numeric Values

arr = [1, 4, 1, 2, 7, 5, 2]
print(Counting_Sort(arr))

# Counting Sort - String Sorting

string = "programemeing"
arr = [ord(i) for i in string]
ans = ""
for i in Counting_Sort(arr):
    ans+=chr(i) 
print(ans)
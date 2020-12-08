import math
def nextGap(gap):
 
    if (gap <= 1):
        return 0
    return (gap // 2) + (gap % 2)

def merge(arr1,arr2,n,m):
    for i in range(n):
        j = 0
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
        if m != 1:
            while arr2[j] > arr2[j+1]:
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
                j+=1
                
                if j>m-2:
                    break
            
def merge2(ar1, ar2, m, n): 
  
    # Iterate through all 
    # elements of ar2[] starting from 
    # the last element 
    for i in range(n-1, -1, -1): 
      
        # Find the smallest element 
        # greater than ar2[i]. Move all 
        # elements one position ahead 
        # till the smallest greater 
        # element is not found  
        last = ar1[m-1] 
        j=m-2
        while(j >= 0 and ar1[j] > ar2[i]): 
            ar1[j+1] = ar1[j] 
            j-=1
   
        # If there was a greater element 
        if (j != m-2 or last > ar2[i]): 
          
            ar1[j+1] = ar2[i] 
            ar2[i] = last 


    
def merge3(arr1,arr2,n,m):
    
    
    gap = math.ceil((n+m)/2)
    arr1.extend(arr2)
    while gap > 0:
        for i in range(n+m):
            if i+gap >= len(arr1):
                break
            if arr1[i] > arr1[i+gap]:
                arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
        gap = nextGap(gap)

 
def merge4(arr1, arr2, n, m):
 
    gap = n + m
    gap = nextGap(gap)
    while gap > 0:
 
        # comparing elements in
        # the first array.
        i = 0
        while i + gap < n:
            if (arr1[i] > arr1[i + gap]):
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
 
            i += 1
 
        # comparing elements in both arrays.
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if (arr1[i] > arr2[j]):
                arr1[i], arr2[j] = arr2[j], arr1[i]
 
            i += 1
            j += 1
 
        if (j < m):
 
            # comparing elements in the
            # second array.
            j = 0
            while j + gap < m:
                if (arr2[j] > arr2[j + gap]):
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
 
                j += 1
 
        gap = nextGap(gap)
 
 
   

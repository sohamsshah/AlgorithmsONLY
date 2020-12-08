def rearrange(arr):
    n = len(arr)
    for i in range(n):
        
        if i%2 == 0:
            val = arr.pop(0)
            arr.append(val)
            
        else:
            val = arr.pop(n-2)
            arr.append(val)
        n-=1
        print(arr)
    return arr


            
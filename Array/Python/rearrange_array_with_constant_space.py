def arrange(arr, n): 
    #Your code here
    for i in range(0, n): 
        arr[i] += (arr[arr[i]] % n) * n
    for i in range(n):
        arr[i] = int(arr[i] / n) 
    return arr

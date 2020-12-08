def rearrange(arr,n):
    for i in range(n):
        arr[arr[i]% n] += i
    for i in range(n):
        arr[i] = arr[i]//n
    return arr
def merge(arr1,arr2,n,m):
    for i in range(n):
        j = 0
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
        print(arr1, arr2, j)
        while arr2[j] > arr2[j+1]:
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
            j+=1
            print(arr1, arr2, j)
            if j>m-2:
                break
merge([1,4,7,8,10], [2,3,9], 5,3)
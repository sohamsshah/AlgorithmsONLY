def majorityWins(arr, n,  x,y):
    # code here
    f_x=0
    f_y=0
    for i in arr:
        if i==x:
            f_x+=1
        if i==y:
            f_y+=1
    if f_x > f_y:
        return x
    elif f_y > f_x:
        return y
    else:
        return min(x,y)
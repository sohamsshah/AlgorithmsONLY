#User function Template for python3
def right(matrix, r, c_start, c_end):
    arr = []
    for i in range(c_start, c_end+1):
        arr.append(matrix[r][i])
    return arr
def left(matrix, r, c_start, c_end):
    arr = []
    for i in range(c_end, c_start-1,-1):
        arr.append(matrix[r][i])
    return arr
def up(matrix, r_start, r_end, c):
    arr = []
    for i in range(r_end, r_start-1,-1):
        arr.append(matrix[i][c])
    return arr
def down(matrix, r_start, r_end, c):
    arr = []
    for i in range(r_start, r_end+1):
        arr.append(matrix[i][c])
    return arr
def spirallyTraverse(matrix, r, c): 
    # code here
    ans = []
    r_start,c_start = 0,0
    r_end,c_end = r-1,c-1
    for _ in range(r//2+1):
        
        ans.extend(right(matrix,r_start,c_start, c_end))
        r_start+=1
        if r_start > r_end:
            break
            
        ans.extend(down(matrix,r_start,r_end,c_end))
        c_end-=1
        if c_start > c_end:
            break
        
        ans.extend(left(matrix,r_end,c_start, c_end))
        r_end-=1
        if r_start > r_end:
            break
            
        ans.extend(up(matrix,r_start,r_end, c_start))
        c_start+=1
        if c_start > c_end:
            break
        
    return ans
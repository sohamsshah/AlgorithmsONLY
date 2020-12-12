## Problem Explanations

### 1. [Rotate Array](https://leetcode.com/problems/rotate-array/)

Problem: Return a Rotated array. 

* #### Approach 1:

Logic: We have to rotate *arr* of length *n* by *d* units. We run a loop and linearly swap i and i+1 by using a temporary variable.

Complexity: O(n*d)

Space: O(1)

* #### Approach 2:

Logic: We will utilize an extra array to store the *d* popped elements and then append that array to the main. 

Complexity: O(d)

Space: O(d)

* #### Approach 3:

Logic: Instead of moving one by one, we divide the array into different sets and size of each set of size = gcd(n,d). Shift element of each set once.

Example: arr = [1,2,3,4,5,6,7,8,9,10,11,12], n=12, d=3

split = gcd(12,3)=3 (Note take d=d%n)

Sets formed: [1,4,7,10], [2,5,8,11] and [3,6,9,12]. Each element is at distance *d*.

Do a total of *d* shifts to swap a total of *n* elements.

``` g_c_d = gcd(d, n)
    for i in range(g_c_d):
        # move i-th values of blocks 
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
 ```

Complexity: O(n)

Space: O(1)

Refer: GFG, LeetCode

---

### 2. [Reverse Array](https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/)

Problem: Return a reversed array.

* #### Approach 1:

Logic: Use temporary array and pop all the elements from primary array to that. Return it.

Complexity: O(n)
Space: O(n)

* #### Approach 2:

Logic: Take two pointers start and end at 0th and n-1th index respectively. Swap (start, end), increment them until middle element is reached. 

* #### Approach 3:

Logic: Use Recursion to solve this. If start >= end, return. Else, keep swapping the start and end and recursively calling the function on start+1 and end-1 indices.
Complexity: O(n)
Space: O(1)



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

Refer: GFG, LeetCode


---

## 3. [Range Sum Queries](https://www.geeksforgeeks.org/range-sum-queries-without-updates/)

Problem: Finding sum in a range. 

Logic: Use Prefix Sum Array to solve this. It takes O(n) time and O(n) space to crate it. But once made, can tackle multiple queries in O(1).

Complexity: O(n)
Space: O(n)
Time for queries: O(1)

Refer: GFG

---


## 4. [Equilibrium Point in an Array](https://www.geeksforgeeks.org/equilibrium-index-of-an-array/)

Problem: Return Equilibrium index of an array.

Logic: Equilibrium index is an index where the sum of all values on left of it and sum of all values on right of it is equal. First, we calculate total sum. Then we iterate through the array, calculate the left sum and update. At each iteration, we check if left sum == (total - left sum - A[i]). If we find such index, we return it.

Complexity: O(n)

Refer: GFG

---

## 5. [Leaders in an Array](https://www.geeksforgeeks.org/leaders-in-an-array/)

Problem: Return the leader in an array.

Logic: Element is a leader if it is greater than or equal to all the elements on its right side. So we start from the end of the array. Keep iterating and adding to a new array called leaders by checking and keeping track of *right maximum* variable.

Refer: GFG, LeetCode

---

## 5. [Convert to a Wave](https://www.geeksforgeeks.org/sort-array-wave-form-2/)

Problem: Given an unsorted array of integers, sort the array into a wave like array. An array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

Logic: swap(i,i+1) and jump index by +2

Refer: GFG

---

## 6. [Subarray with a given sum with NO NEGATIVE VALUES](https://www.geeksforgeeks.org/find-subarray-with-given-sum/)

Problem: Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.

Logic: Since there are no negative values, we can linearly iterate through the array and follow the algorithm. While low <= high, we check if current sum == sum. If it matches, return (low, high). Else, if current sum > sum, decrement current sum by arr[low]. 

```
def subArraySum(arr, n, sum): 
    low = 0 
    high = 0
    curr_sum = arr[low]
    
    while low <= high and high <= n - 1:
        if curr_sum == sum:
            print(low,high)
        elif curr_sum < sum:
            high = high + 1
            curr_sum = curr_sum + arr[high]
        else:
            curr_sum = curr_sum - arr[low]
            
    print(-1)
```

Refer: GFG

---

## 7. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

Problem: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Logic: Calculate sum(min(left_max[i], right_max[i]). Make prefix sum arrays for left_max and right_max arrays.

Example: 

<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png">

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Refer: LeetCode , GFG

---

## 8. [Rearrange in Min-max Form from a Sorted Array](https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/)

Problem: Given a sorted array of positive integers, rearrange the array alternately i.e first element should be the maximum value, second minimum value, third-second max, fourth-second min and so on.

Logic: 

For Even indices - Pop from TOP and append to the array.

For Odd indices -  Pop from n-1 and append. Decrement n after each otheration so it always points to the right value.

Refer: GFG

---

## 9. [Kadane's Algorithm](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)

Problem: Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

Logic: Simple idea of the Kadane’s algorithm is to look for all positive contiguous segments of the array (max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). Each time we get a positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far.

Kadane's Algorithm:

```
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far
```
Complexity: O(n)

Refer: GFG

---


     











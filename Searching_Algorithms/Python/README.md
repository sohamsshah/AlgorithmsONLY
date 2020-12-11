## Problem Explanations

### 1. [Binary Search](https://practice.geeksforgeeks.org/problems/binary-search-1587115620/1/?track=dsa-workshop-1-search-sort&batchId=308)
Problem: Search for x in a List 
Logic: To solve it in O(logn) complexity, we follow the following algorithm.

**Algorithm**:
1. Find start, end and mid.
2. While start <= end; loop through.
3. mid = l + (r-l)/2
4. Check if arr[mid] == key; return.
5. if arr[mid] < key: start = mid+1 else: end = mid-1

Complexity: O(logn)

Refer: GFG, Aditya Verma

---

### 2. [Binary Search in descending Array](https://www.youtube.com/watch?v=YbkELwnGRdo&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=3)
Problem: Search for x in a List that is sorted in Descending order. 
Logic: To solve it in O(logn) complexity, we follow the following algorithm.

**Algorithm**:
1. Find start, end and mid.
2. While start <= end; loop through.
3. mid = l + (r-l)/2
4. Check if arr[mid] == key; return.
5. if arr[mid] > key: start = mid+1 else: end = mid-1

Complexity: O(logn)

Refer: GFG, Aditya Verma

---

### 3. [First and Last Occurences of an Element in a Sorted List](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
Problem: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1]. 

Logic: The idea is that since the list is sorted, the first occurence of the element will always lie on left side of found element (if any). And the last occurence will be on the right side. Now, if arr[mid] == key, then we store its index to a variable and move *left* to search first occurence and *right* to get the last occurence. To solve it in O(logn) complexity, we follow the following algorithm.

**Algorithm**:
1. If arr[mid] == key, store it in result variable and end = mid-1 for first occurence.
2. If arr[mid] == key, store it in result variable and start = mid+1 for first occurence.
3. Elsewhere, do normal Binary Search.

Complexity: O(logn)

Refer: GFG, LeetCode, Aditya Verma

---

### 4. [Count of an element in a Sorted Array](https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/)
Problem: Return number of count of a particular element in a given Sorted Array. 
Logic: To solve it in O(logn) complexity, we follow the following algorithm.

**Algorithm**:
1. Find the index of First Occurence of the element; store as first.
2. Find the index of First Occurence of the element; store as last.
3. Return (last-first)+1

Complexity: O(logn)

Refer: GFG, Aditya Verma

---

### 5. [Number of times a Sorted Array is Rotated](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)
Problem: Return number of times a sorted array is rotated. 
Logic: The Pivot element is actually at the index of minimum value of the array. The minimum value will be smaller than both its neighbors. Since array is rotated, the array is unsorted. If we find mid, then one half will be unsorted, while other half will be sorted. We have to consider only the unsorted part as the minimum element will be there. To solve it in O(logn) complexity, we follow the following algorithm.

**Algorithm**:
1. Find mid = (start+end)/2
2. nxt = (mid+1)%n, prev = (mid-1+n)%n
3. Return arr[mid], if nums[mid]<=nums[prev]
4. Return arr[mid+1], if nums[mid]>=nums[nxt]
5. Else, go towards unsorted part.
6. if nums[mid] >= nums[l]: l = mid + 1 
   elif nums[mid] <= nums[r]: r = mid - 1

Complexity: O(logn)

Refer: GFG, Aditya Verma, LeetCode

---

### 6. [Find an Element in a Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
Problem: Return index of a particular element in a given Sorted Array (Search operation) 
Logic: To solve it in O(logn) complexity, we follow the following algorithm.

**Algorithm**:
1. Find the index of Pivot Element (from where the Array is rotated); store as pivot.
2. Apply Binary Search in both halves.
3. BS(arr, 0, pivot-1, key) 
   BS(arr, pivot, n-1, key)

Complexity: O(logn)

Refer: GFG, Aditya Verma, LeetCode

---

### 7. [Search in a nearly Rotated Sorted Array](https://www.geeksforgeeks.org/search-almost-sorted-array/)
Problem: Return index of a particular element in a given Nearly Sorted Array (Search operation). In a Nearly Sorted array, arr[i] may be present at arr[i+1] or arr[i-1].
Logic: At each arr[mid] search, we also look for indices arr[mid+1] and arr[mid-1]. We take for edge conditions so that it doesnt go out of bound. Instead of updating start and end pointers by one unit from *mid*, here we update by +2 or -2. To solve it in O(logn) complexity, we follow the following algorithm.

**Algorithm**:
1. if arr[mid] == key: return mid.
2. if mid>=l and arr[mid-1] == k: return mid-1
3. if mid <=r and arr[mid+1] ==k: return mid+1 
4. if mid > k: r = mid-2; elif mid < k: l = mid+2

Complexity: O(logn)

Refer: GFG, Aditya Verma, LeetCode

---













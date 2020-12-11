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









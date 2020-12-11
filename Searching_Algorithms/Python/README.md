## Problem Explanations

### 1. [Binary Search](https://practice.geeksforgeeks.org/problems/binary-search-1587115620/1/?track=dsa-workshop-1-search-sort&batchId=308)
Problem: Search for x in a List 
Logic: To solve it in O(logn) complexity, we follow the following algorithm.

**Logic**:
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

**Logic**:
1. Find start, end and mid.
2. While start <= end; loop through.
3. mid = l + (r-l)/2
4. Check if arr[mid] == key; return.
5. if arr[mid] > key: start = mid+1 else: end = mid-1

Complexity: O(logn)






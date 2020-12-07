# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:49:09 2020

@author: Soham Shah
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        cnt = 0
        for i in nums:
            if candidate != i:
                cnt-=1
            else:
                cnt+=1
            if cnt==0:
                candidate = i
                cnt+=1
        return (candidate)
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:56:46 2020

@author: Soham Shah
"""

from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judges = defaultdict(list)
        for i in range(1, N+1):
            judges[i] = [0,0]
        for i in trust:
            judges[i[1]][0]+=1
            judges[i[0]][1]+=1
        for i in judges:
            if judges[i][0] == N-1 and judges[i][1] == 0:
                return i
        return -1
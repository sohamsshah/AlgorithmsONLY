# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:37:49 2020

@author: Soham Shah
"""

matrix = [[10, 20, 30, 40],
          [15, 25, 35, 45],
          [27, 29, 37, 48],
          [32, 33, 39, 50]]


target = 32

i = 0
j = len(matrix[0]) - 1

while j >= 0 and i <= len(matrix):
    if matrix[i][j] > target:
        j-=1
    elif matrix[i][j] == target:
        print("Found", matrix[i][j], i, j)
        break
    else:
        i+=1
        
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 00:00:26 2020

@author: Soham Shah
"""

# Letter Case Permutation

string = "a1B2"
ans = []

def solve(input, output):
    if not input:
        ans.append(output)
        return
    if input[0].isalpha():
        output1 = output[:]
        output2 = output[:]
        output1+=(input[0].lower())
        output2+=(input[0].upper())
        input = input[1:]
        solve(input, output1)
        solve(input, output2)
    else:
        output1 = output[:]
        output1+=(input[0])
        input = input[1:]
        solve(input, output1)

solve(string, "")
        
    
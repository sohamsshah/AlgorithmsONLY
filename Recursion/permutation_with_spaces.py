# -*- coding: utf-8 -*-

# Permutation with Spaces

string = "ABC"
ans = []

def solve(input, output):
    if not input:
        ans.append(output)
        return
    output1 = output[:]
    output2 = output[:]
    output1+=("_"+ input[0])
    output2+=(input[0])
    input = input[1:]
    solve(input, output1)
    solve(input, output2) 

solve(string[1:], string[0])
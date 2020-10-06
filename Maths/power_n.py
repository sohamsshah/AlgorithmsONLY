# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 12:16:08 2020

@author: Soham Shah
"""

ans = 1
x = 2
n = -10
nn = -10

if nn < 0:
    nn*=-1
while nn > 0:
    if nn%2 == 0:
        x*=x
        nn//=2
    else:
        ans*=x
        nn-=1
if n < 0:
    print(1/ans)
else:
    print(ans)
    
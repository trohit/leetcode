#!/usr/bin/env python3
# 46. Permutations
# https://leetcode.com/problems/permutations
# -*- coding: utf-8 -*-
"""
>>> from itertools import permutations
>>> for i in permutations([1,2,3]):
...     print(i)
...
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
>>>
"""
def get_permutations(arr):
  
    def swap(arr, i, j):
        print(f"{i}<>{j}")
        (arr[i], arr[j]) = (arr[j], arr[i])
    
    def helper(a, i, res, lvl = 0):
        print(f"{' ' *lvl*2}lvl:{lvl} i:{i} a:{a}")
        # base case / leaf node
        if i == len(a) - 1:
            print(f"{' ' *lvl*2}appending a:{a}")
            res.append(a.copy())
            return
        
        # intermediate / nested node
        # print(f"{' ' *lvl*2}ph1 sl:{sl} a:{a}")
        for j in range(i, len(arr)):
            swap(a, i, j)
            helper(a, i+1, res, lvl+1)
            swap(a, i, j) # unswap

    res = []
    helper(arr, 0, res)
    return res

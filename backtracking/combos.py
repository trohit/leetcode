#!/usr/bin/env python3
"""
# n choose k
# T: O(k.2^n)
n = 4
k = 2
# of combos = n!/(n-k)!.k!

Output:
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]] 
"""

from typing import List
def helper(i:int, sl:list[int], res:list[int], n:int, k:int)->None:
    # base
    if len(sl) == k:
        res.append(sl.copy())
        return
    if i > n: return

    # inter
    # incl i
    sl.append(i)
    helper(i+1, sl, res, n, k)

    # dont include i
    sl.pop()
    helper(i+1, sl, res, n, k)

def combos(n, k):
    sl, res = [], []
    helper(1, sl, res, n, k)
    return res

# main
a = [1,2,3]
res = combos(4, 2)
print(res)

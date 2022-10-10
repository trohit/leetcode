#!/usr/bin/env python3

from typing import List
# n choose k
# T: O(k.2^n)
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

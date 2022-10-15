#!/usr/bin/env python3
"""
# n choose k
# T: O(k.2^n)
n = 4
k = 2
# of combos = n!/(n-k)!.k!

Output:
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]] 

from itertools import combinations
for i in combinations([1,2,3], 2):
    print(i)
(1,2)
(1,3)
(2,3)
"""

from typing import List

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

# alternate optimal approach O(k.C(n,k)) exists
# Time: O(k * C(n, k))
def combinations2(n, k):
    combs = []
    helper2(1, [], combs, n, k)
    return combs

def helper2(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    if i > n:
        return
    
    for j in range(i, n + 1):
        curComb.append(j)
        helper2(j + 1, curComb, combs, n, k)
        curComb.pop()

# main
a = [1,2,3]
res = combos(4, 2)
print(res)

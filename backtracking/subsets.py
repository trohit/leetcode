#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T:O(2^n.n)
S:O(n)
Max items in Subset: 2^n
Motto: To choose or skip an elm, thats the q

https://leetcode.com/problems/subsets/

https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
s, n = [1,2,3], len(s)
Subsets-1
for i in range(n+1):
	it = [ combinations(s, i) ]
	for j in it:
		for k in j:
			print(k)

Subsets-2
it = [ combinations(s, n) for n in range(len(s)+1) ]
for i in it:
     for j in i:
             print(j)
Subsets-3
ss = [it for it in chain.from_iterable(combinations(s, n) for n in range(len(s)+1))]

Output:
choose elm 1
  choose elm 2
    choose elm 3
      appending [1, 2, 3]
    skip elm 3
      appending [1, 2]
  skip elm 2
    choose elm 3
      appending [1, 3]
    skip elm 3
      appending [1]
skip elm 1
  choose elm 2
    choose elm 3
      appending [2, 3]
    skip elm 3
      appending [2]
  skip elm 2
    choose elm 3
      appending [3]
    skip elm 3
      appending []
[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
"""

def helper(nums, i, sl, res, lvl = 0):
    # base case or leaf nodes
    n = len(nums)
    if i >= n:
        print(f"{' '*2*lvl}appending {sl}")
        res.append(sl.copy())
        return

    # intermediate nodes case
    print(f"{' '*2*lvl}choose elm {nums[i]}")
    sl.append(nums[i])
    helper(nums, i+1, sl, res, lvl + 1)
    sl.pop() # NOTE: unchoose elm while unwinding the stack 

    print(f"{' '*2*lvl}skip elm {nums[i]}")
    helper(nums, i+1, sl, res, lvl + 1)

def subsets(nums):
    res, sl = [], [] # res holds all output, sl is the slate to store tmp output
    helper(nums, 0, sl, res)
    print(res)

#main
nums = [1,2,3]
#chars = ['a','b','c']
subsets(nums)

#!/usr/bin/env python3
# https://www.youtube.com/watch?v=s7AvT7cGdSo
# T:O(n!) as at there are n steps viz 3.2.1 subprobs and at last lvl there will be addl. time const n to copy the res str O(n!+n)
# S:O(n.n!) as there are n! perms and storing each perm takes n space.
"""
cba
bca
acb
cab
bac
abc
"""
def permute(nums:list)->None:
    res = []
    if len(nums) == 1:
        res.append(nums[:])
        return res
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res
# main
res = permute(['a','b','c'])
[print("".join(i)) for i in res]

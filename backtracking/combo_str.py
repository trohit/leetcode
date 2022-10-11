#!/usr/bin/env python3
"""
from itertools import combinations as combo
for i in combo([1,2,3], 2):
    print(i)
(1,2)
(1,3)
(2,3)

Output:

hlp:l:0i:0 sl:
sl.apnd 0=>a sl:[]
 hlp:l:1i:1 sl:a
 sl.apnd 1=>b sl:['a']
  hlp:l:2i:2 sl:ab
  >> sl:ab
 sl.apnd 2=>c sl:['a']
  hlp:l:2i:3 sl:ac
  >> sl:ac
 sl.apnd 3=>d sl:['a']
  hlp:l:2i:4 sl:ad
  >> sl:ad
sl.apnd 1=>b sl:[]
 hlp:l:1i:2 sl:b
 sl.apnd 2=>c sl:['b']
  hlp:l:2i:3 sl:bc
  >> sl:bc
 sl.apnd 3=>d sl:['b']
  hlp:l:2i:4 sl:bd
  >> sl:bd
sl.apnd 2=>c sl:[]
 hlp:l:1i:3 sl:c
 sl.apnd 3=>d sl:['c']
  hlp:l:2i:4 sl:cd
  >> sl:cd
sl.apnd 3=>d sl:[]
 hlp:l:1i:4 sl:d
 !! i:4 k:2n:4
['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
"""
def combo(letters, k):
    n = len(letters)
    res, sl = [], [] # res is result, sl is a temp slate
    helper(letters, 0, sl, res, n, k)
    return res


def helper(letters, i, sl, res, n, k, lvl = 0):
    t = "".join(sl)
    print(f"{' '*lvl}hlp:l:{lvl}i:{i} sl:{t}")
    # base
    if len(sl) == k:
        print(f"{' '*lvl}>> sl:{t}")
        #res.append(t.copy()) # deep copy needed if we dont use 't'
        res.append(t)
        return
    if i >= n:
        print(f"{' '*lvl}!! i:{i} k:{k}n:{n}")
        return
    #inter
    for j in range(i, n):
        print(f"{' '*lvl}sl.apnd {j}=>{letters[j]} sl:{sl}")
        sl.append(letters[j])
        helper(letters, j+1, sl, res, n, k, lvl+1)
        sl.pop()

# main
l = "abcd"
letters = list(l) # sentence
res=combo(letters, 2)
print(res)

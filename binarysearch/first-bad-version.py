'''
L278
https://leetcode.com/problems/first-bad-version/
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
Easy

Runtime: 24 ms, faster than 95.10% of Python3 online submissions for First Bad Version.
Memory Usage: 14.3 MB, less than 10.12% of Python3 online submissions for First Bad Version.
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

'''
Approach: Special case of binary search where dup items are possible and when we find a matching elm(bad) its not enough as
we may need to find the first bad version which could be to the right of the elm we just matched.
So possible cases follow.

Legend: 
  g for good item
  b for bad item
  ptrs l,m,r = lo, mid, hi
  
case 1: gbb
         ^
         m
         we dont know if 1st bad, so include m in search window
         so, r = m instead of r = m - 1
case 2: ggb
         ^
         m
         we know everything upto m is good, so search after m
         l = m + 1 just like in mormal binary search 
when l == r: loop breaks
as bad is guaranteed, return l or r, doesnt matter

Tip: check simple case of 2 elms [g,b]
if it works, then algo wont loop infinitely
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1, n
        while l < r:
            # mid = l + ( (r-l) //2 )
            mid = l + ( (r-l) >> 1 ) # faster due to right shift
            is_bad = isBadVersion(mid)
            if is_bad == True:
                r = mid # mid could be the 1st bad version
            else: # is_bad == False:# xprint(">need to search to the right")
                l = mid+1 # as mid isnt bad
        return r # can return l or r, doesnt matter, its the same

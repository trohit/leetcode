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
Runtime: 37 ms, faster than 31.74% of Python3 online submissions for First Bad Version.
Memory Usage: 14.4 MB, less than 10.12% of Python3 online submissions for First Bad Version.
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1, n
        # edge
        if n == 1:
            if isBadVersion(n) == True:
                return n
            else:
                return -1
            
        while l < r:
            mid = l + ( (r-l) //2 )
            xprint(f"{l}.{mid}.{r}", end=",")
            is_bad = isBadVersion(mid)
            xprint(f"{mid} = {is_bad}")
            if is_bad == True:
                if mid == 1:
                    xprint("very 1st sample bad")
                    return mid
                elif mid > 1:
                    if isBadVersion(mid-1) == False:
                        xprint("mid is first bad version")
                        return mid
                    elif isBadVersion(mid-1) == True:
                        # not 1st bad, search left
                        xprint("<")
                        r = mid-1
            elif is_bad == False:
                # need to search to the right
                xprint(">")
                l = mid+1
        if isBadVersion(mid-1) == True:
            xprint("sample 1 left of mid")
            return mid-1
        elif isBadVersion(mid+1) == True:
            xprint("sample 1 right of mid")
            return mid+1
        else:
            xprint("last suspect")
            return mid+1
        
        

'''
# https://leetcode.com/problems/the-kth-factor-of-n/
#simple way
def xprint(*args, **kwargs):
    return
    print("".join( map(str, args)), **kwargs)
    
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k < 1: return -1 # invalid value for k
        if n < 1: return -1  # invalid value for n
        num_factors_seen = 0
        for i in range(1,n+1):
            xprint(f"checking {i}")
            if n%i == 0:
                xprint(f"num_factors_seen: {num_factors_seen} {i}")
                num_factors_seen += 1
            if num_factors_seen == k:
                xprint(f"{k}th factor of {n} is {i}")
                return i
        return -1
"""
# faster way
# ex: 4th factor of 30  = 1 2 3 (5) 10 15 30 
# ex: 4th factor of 30  = 1 2 3 (5) 10 15 30 
# loop from 1 .. n//2
# if n/i == 0 and i*j = n then j is also a factor
# if 2 can divide 30, so can 30/2 => 15 is also a factor
# so we only need to loop uptil sqrt(n) to get all factors 

from math import sqrt, floor
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ll = []
        tk = k # tmp k
        if n < 1 or k < 1: return -1 
        sqrt_n = int(floor(sqrt(n)))
        xprint(f"1..{sqrt_n+1}")
        for i in range(1,sqrt_n+1):
            xprint(f"trying {n}/{i} with rem k {tk}")
            if n%i == 0:
                tk-=1
                ll.append(i)
                xprint(f"tk:{tk} with i:{i}")
                j = int(n/i)
                if i != 1 and j!=i and n%j == 0:
                    tk-=1
                    ll.append(j)
                    xprint(f"tk {tk} with j:{j}")
        ll.append(n) # n is a factor of itself
        ll.sort()
        xprint(f"ll:{ll}")
        if len(ll) >= k:
            return ll[k-1]
        
        return -1
            
            
        

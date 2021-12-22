# https://leetcode.com/problems/sqrtx/
'''
times out as its brute force
time: O(n)
space: O (1)
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)
    
class Solution:
    def mySqrt(self, x: int) -> int:
        # edge cases
        if x == 0 or x==1 : return x
        i = 2
        while True:
            psq = i*i #  possible square
            xprint(f"x:{x} i:{i}  psq:{psq}")
            if psq == x:
                return i
            elif psq > x:
                return i-1
            i+=1
        return -1
        

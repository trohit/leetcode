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
        
# another attempt
'''
times out and doesnt work for 2147483647
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)

def binsearch(x):
    st = 2
    end = x//2
    while st <= end:
        mid = int(st + (end-st)/2)
        sq = mid*mid
        xprint(f"x:{x} sq: {sq} st:{st} mid:{mid} end:{end}")
        # import pdb;pdb.set_trace()
        if sq > x:
            xprint("<")
            end = mid-1
        elif sq < x:
            xprint(">")
            st = mid+1
    return mid
    
class Solution:
    def mySqrt(self, x: int) -> int:
        # edge cases
        if x == 0 or x==1 or x==2 : return x
        res = binsearch(x)
        return res

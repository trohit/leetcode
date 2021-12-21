# https://leetcode.com/problems/powx-n
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)
    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        xprint(f"x:{x} n:{n}")
        sign = 1
        is_neg_exp = False
        # edge cases
        if n == 0: return 1
        if n == 1: return x
        if n < 0: 
            n *= -1
            is_neg_exp = True
        # if x < 0 and n%2: sign = -1
        if is_neg_exp:
            res = 1 / (sign * x * self.myPow(x, n-1))
            print(f"resturning {res}")
            return res
        else:
            xprint(sign)
            return 1 * sign * x * self.myPow(x, n-1)
            
        
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)
    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # xprint(f"x:{x} n:{n}")
        m = 1
        if n < 0: is_fraction = True
        # edge cases
        if n == 0: return 1
        if n == 1: return x
        while n!=0:
            m = m*x
            if n>0:
                n = n-1
            elif n <0:
                n = n+1
        if is_fraction == False:
            return m
        else:
            return 1/m


'''
a non-recursive solution but does not pass this testcase
0.00001
2147483647

291 / 304 test cases passed.
Time Limit Exceeded
'''
   print("".join(map(str,args)), **kwargs)
    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # xprint(f"x:{x} n:{n}")
        m = 1
        is_fraction = False
        if n < 0: is_fraction = True
        # edge cases
        if n == 0: return 1
        if n == 1: return x
        while n!=0:
            m = m*x
            if n>0:
                n = n-1
            elif n <0:
                n = n+1
        if is_fraction == False:
            return m
        else:
            return 1/m

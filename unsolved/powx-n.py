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
        
        
# optimal solution
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)
    
class Solution:
    def fastPow(self, x,n):
        if n == 0: return 1  
        if x == 0: return 0 # only for optimization, from 36ms -> 32 ms
        if n == 1: return x # only for optimization, from 36ms -> 32 ms
        xprint(f"> x:{x} n:{n}")
        half = self.fastPow(x, n//2)
        if n%2 == 0:
            xprint(f">> x:{x} n:{n} h:{half} even")
            return half * half
        else:
            xprint(f">> x:{x} n:{n} h:{half} odd")
            return half * half * x
        
    def myPow(self, x: float, n: int) -> float:
        xprint(f"x:{x} n:{n}")
        N = n
        if N < 0:
            x = 1/x
            N=-N
        return self.fastPow(x,N)

# even faster 28 ms faster than 85%
# builds on subdivinding into 4 instead of 2 
# big O remains same
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)
    
class Solution:
    def fastPow(self, x,n):
        if n == 0: return 1
        if x == 0: return 0
        if n == 1: return x
        xprint(f"> x:{x} n:{n}")
        fourth = self.fastPow(x, n//4)
        if n%4 == 0:
            xprint(f">> x:{x} n:{n} h:{fourth} even")
            return fourth * fourth * fourth * fourth
        elif n%4 == 1:
            xprint(f">> x:{x} n:{n} h:{fourth} odd")
            return fourth * fourth * fourth * fourth * x
        elif n%4 == 2:
            xprint(f">> x:{x} n:{n} h:{fourth} 2")
            return fourth * fourth * fourth * fourth * x * x
        elif n%4 == 3:
            xprint(f">> x:{x} n:{n} h:{fourth} 3")
            return fourth * fourth * fourth * fourth * x * x * x
            
        
    def myPow(self, x: float, n: int) -> float:
        xprint(f"x:{x} n:{n}")
        N = n
        if N < 0:
            x = 1/x
            N=-N
        return self.fastPow(x,N)    

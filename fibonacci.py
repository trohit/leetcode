# https://leetcode.com/problems/fibonacci-number/
class Solution:
    t = [0] * 31
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n ==1 or n == 2:
            return 1
        if self.t[n]:
            return self.t[n]
        self.t[n] = self.fib(n-1)+ self.fib(n-2)
        return self.t[n] 
        

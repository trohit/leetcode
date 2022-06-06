'''
https://leetcode.com/problems/fibonacci-number
509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
Constraints: 0 <= n <= 30

Runtime: 29 ms, faster than 92.83% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 53.96% of Python3 online submissions for Fibonacci Number.
'''
class Solution:
        
    def fib(self, n: int) -> int:
        self.dp = [-1]* (n+1)
        if n == 0 or n == 1: return n
        self.dp[0] = 0
        self.dp[1] = 1
        return self._fib(n)
    
    def _fib(self, n:int)-> int:
        # print(f"computing {n}, dp:{self.dp}, {len(self.dp)}")
        # if n == 0: return 0
        # if n == 1: return 1
        if self.dp[n] == -1:
            self.dp[n] = self._fib(n-1) + self._fib(n-2)
        return self.dp[n]
        

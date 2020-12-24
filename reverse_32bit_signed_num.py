# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:56:12 2020
@author: talukr
https://leetcode.com/problems/reverse-integer/submissions/
"""

class Solution:
    def reverse(self, x: int) -> int:
        max_pos = 2**31-1
        max_neg = -1* 2**31
        is_neg = False
        if x == 0 or x > (2**31)-1:
            return 0
        elif x < 0:
            x *= -1
            is_neg = True
        y = str(x)[::-1]
        while y[0] == '0':
            y = y[1:]
        if is_neg:
            y = int(y)*-1
        if int(y) > max_pos or int(y) < max_neg:
            return 0
        print(y)
        print(2**31)

        return y

#main
num = 1534236469
s = Solution()
print(s.reverse(num))

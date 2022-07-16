"""
https://leetcode.com/problems/roman-to-integer/
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Runtime: 64 ms, faster than 69.85% of Python3 online submissions for Roman to Integer.
Memory Usage: 14 MB, less than 30.61% of Python3 online submissions for Roman to Integer.
"MCMXCIV"
1994
"""
class Solution:
    def getval(self, rch):
        rv_dd = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
            
        if rch in rv_dd.keys():
            return rv_dd[rch]
        return 0
    
    def romanToInt(self, s: str) -> int:
        ll = []
        for i in range(len(s)):
            num = self.getval(s[i])
            if len(ll): # not 1st time
            # if i:
                # if spec cases, replace last num
                if ll[-1] == 1 and num == 5:
                    ll[-1] = 4
                elif ll[-1] == 1 and num == 10:
                    ll[-1] = 9
                elif ll[-1] == 10 and num == 50:
                    ll[-1] = 40
                elif ll[-1] == 10 and num == 100:
                    ll[-1] = 90
                elif ll[-1] == 100 and num == 500:
                    ll[-1] = 400
                elif ll[-1] == 100 and num == 1000:
                    ll[-1] = 900
                else: # if no spec case, just stoe the val 
                    # print(f"{ll}:fappending {num}")
                    ll.append(num)
            else: # first time
                # print(f"{ll}:appending {num}")
                ll.append(num)
        # print(ll)
        tot = sum(ll)
        return tot
        

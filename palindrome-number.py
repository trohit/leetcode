# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        o = x
        n = 0
        pow = 0
        t = x
        if x < 0:
            return False
        while t:
            pow+=1
            t = t//10
        pow-=1
        t = x
        while t > 0:
            rem =  (t%10)
            tt = (rem*10**pow)
            n = tt+n
            t = t // 10
            # print(f"x:{x} n:{n} pow:{pow}" )
            pow-=1
        # print(f"x:{x} n:{n}" )
        if x == n:
            return True
        return False

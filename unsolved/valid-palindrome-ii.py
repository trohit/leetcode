'''
L680
https://leetcode.com/problems/valid-palindrome-ii/
Runtime: 760 ms, faster than 5.01% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.7 MB, less than 17.57% of Python3 online submissions for Valid Palindrome II.
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)

def ispalinrt(s):
    xprint("lft")
    l = 0
    r = len(s)-1
    mismatch_cnt = 0
    while l<r:
        xprint(f"{l}{s[l]}<>{s[r]}{r}", end=":")
        if s[l]!=s[r]:
            if mismatch_cnt == 0:
                xprint("mismatch seen once")
                mismatch_cnt = 1
                r+=1
            else:
                xprint("mismatch : two strikes")
                return False
        l+=1
        r-=1
    return True

def ispalinlt(s):
    xprint("lft")
    l = 0
    r = len(s)-1
    mismatch_cnt = 0
    while l<r:
        xprint(f"{l}{s[l]}<>{s[r]}{r}")
        if s[l]!=s[r]:
            if mismatch_cnt == 0:
                xprint("mismatch seen once")
                mismatch_cnt = 1
                l-=1
            else:
                xprint("mismatch : two strikes")
                return False
        l+=1
        r-=1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        xprint(s)
        res1 = ispalinlt(s)
        res2 = ispalinrt(s)
        return res1 or res2
        

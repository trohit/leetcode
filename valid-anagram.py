'''
https://leetcode.com/problems/valid-anagram
Runtime: 74 ms, faster than 55.70% of Python3 online submissions for Valid Anagram.

'''
class Solution:
    def get_sign(self, s:str)->dict:
        dd = {}
        for i in s:
            if i not in dd:
                dd[i] = 1
            else:
                dd[i] += 1
        return dd        
        
    def isAnagram(self, s: str, t: str) -> bool:
        sdd = self.get_sign(s)
        tdd = self.get_sign(t)
        if tdd == sdd:
            return True
        return False
        

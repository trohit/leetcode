"""
https://leetcode.com/problems/backspace-string-compare/
844. Backspace String Compare
Easy
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""

"""
Qs
1. can there be more backspaces than chars ?

approach 

A:
    1. use a stack and pop strings when '#' seen 
    2. then cmp both result strings
    3. T : O(n)*2 + O(n) ~= O(n)
    4. S : O(n) where n is maxlen of both strings  
    
B:
    1. use the same str space and when '#' seen pop str 
    2. s
class Solution:
    def get_result(self, s:str)->str:
        st = []
        for i in s:
            if i != '#': st.append(i)
            elif i == '#':st.pop()
        return st
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = self.get_result(s)
        s2 = self.get_result(t)
        print(f"s1:{s1}")
        print(f"s2:{s2}")
        
        if s1 == s2: return True
        return False
"""
            
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(s):
            skip = 0
            for ch in reversed(s):
                print(f"ch:{ch}")
                if ch == "#":skip += 1
                elif skip:   skip -= 1
                else: yield ch
            yield None
                    
        for c1, c2 in zip(parse(s), parse(t)):
            print(f"cmp {c1}<>{c2}")
            if c1 != c2: return False
        return True
        # return all(x == y for x, y in itertools.zip_longest(f(s), f(t)))
                
        

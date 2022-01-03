'''
L921
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
Runtime: 28 ms, faster than 85.80% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 14.3 MB, less than 42.57% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
'''
'''
rules
1. An ob has to be before a cb
2. count(ob) = count (cb)
3. if 

edge case
1. if no braces all ok

algo
1. if cb, push and remember pos of ob
2. if ob, pop until a cb is found
3. make a note of all unmatched ob
'''
# just a wrapper print for debugging
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # edge case
        if s == None or s == "":
            return 0
        n = len(s)
        ob_ll = []
        need_ob = 0 
        for i in range(0,n):
            if s[i] == '(':
                ob_ll.append(i)
            elif s[i] == ')':
                if len(ob_ll) != 0:
                    ob_ll.pop() 
                else:
                    # xprint("no matching cb")
                    need_ob+=1
        # if no braces remain all good else return number of braces 
        return len(ob_ll) + need_ob
        

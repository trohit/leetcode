"""
22. Generate Parentheses
Medium
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""

"""
Approach:
use permutations and n choose k where k > n, so duplicates are expected.
Can use brute force backtracking but will result in 2^n.
Instead, we prune paths when we realize that the paths are invalid. Results in a Catalan number complexity.

https://iq.opengenus.org/applications-of-catalan-numbers/
T:
= time to generate each elm * num of elms
= O(4^n/sqrt(n)) lesser than 2^n
S:O(4^n/sqrt(n))
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(o, c, n, sl, res):
            # c1: o == c == n
            if o == c == n:
                tsl = "".join(sl)
                res.append(tsl)
                return
            # c2: if o < n: add o 
            if o < n:
                sl.append('(')
                bt(o+1, c, n, sl, res)
                sl.pop()
            # c3: if c < o: add c 
            if c < o:
                sl.append(')')
                bt(o, c+1, n, sl, res)
                sl.pop()
            
        res = []
        bt(0, 0, n, [], res)
        return res

"""
Brute-force method to generate permutations
Generates all possible combos and checks if any are valid.
complexity os of the order of a catalan number as 
certain exploration paths are pruned as soon as they are deemed to be invalid.

def braces(n):
    def is_valid(a):
        bal = 0
        for c in a:
            if c == '(': bal += 1
            if c == ')': bal -= 1
            if bal < 0: return False
        if bal == 0: return True
        return False

    def gen(n, sl, res):
        # leaf node / base condition
        if len(sl) == 2 * n:
            tsl = "".join(sl)
            res.append(tsl)
        return # return any which ways if the length matches 2 * n
        # mgr node
        sl.append("(")
        gen(n, sl, res)
        sl.pop()
        
        sl.append("(")
        gen(n, sl, res)
        sl.pop()
        
    # function
    res = []
    gen(n, [], res)
    return res
"""

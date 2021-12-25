'''
L1249
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Runtime: 5164 ms, faster than 5.02% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
Memory Usage: 16.9 MB, less than 12.00% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
'''
def xprint(*args, **kwargs):
    return
    # print("".join(map(str,args)), **kwargs)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        indexes_to_rm = []
        bal = 0
        
        for k,i in enumerate(s):
            # open brace, push to stack
            xprint(f"{k}:{i} st:{st} bal:{bal}", end=":")
            if i == '(':
                bal += 1
                xprint("ob, push to stack")
                st.append(k)
            # close brace must match open brace, else discard
            elif i == ')':
                if bal <= 0: # unbalanced bal, discard
                    xprint(f"unbal cb discarding at {k}:{i} ")
                    indexes_to_rm.append(k)
                    continue
                if bal > 0: # ((()) pop to match ob
                    res = st.pop()
                    bal -= 1
                    xprint(f"popped last '(' at {res}:{s[res]} bal:{bal}")
            # any other char
            else:
                xprint(f"ignoring {k}:{i}")
        # any unmatched trailing ob must be discarded
        indexes_to_rm.extend(st)
        xprint(f"st:{st} bal:{bal}")
        # remove any unbalanced obraces starting from right
        while bal != 0:
            xprint(f"at end popping unbal {bal}")
            res = st.pop()
            bal-=1
                
                
        xprint(f"indexes_to_rm:{indexes_to_rm}")
        # make a new str
        new_str_ll = []
        for k,v in enumerate(s):
            xprint(f"{k}:{v}")
            if k not in indexes_to_rm:
                new_str_ll.append(v)
        xprint(new_str_ll)
        new_s = "".join(new_str_ll)
        return new_s
        

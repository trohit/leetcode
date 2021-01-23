
"""
Runtime: 32 ms, faster than 94.23% of Python3 online submissions for Add Strings.
Memory Usage: 14.4 MB, less than 69.62% of Python3 online submissions for Add Strings.


n1:100
n2: 10
-------
   110
-------

   1
n1:99
n2:99
-----
  198
  
   1
n1:98
n2: 2
-----
  100
"""
        
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # longer string will be num1
        if len(num2) > len(num1):
            num1, num2 = num2, num1
                        
        # pad num2 with 0's
        while len(num2) != len(num1):
            num2 = "0" + num2

        # print(f" num1:{num1}")
        # print(f" num2:{num2}")
        num3 = ""
        carry = n1 = n2 = ncarry = 0
        for i in reversed(range(len(num1))):
            n1 = int(num1[i])
            n2 = int(num2[i])
            # print(f"n1:{n1} n2:{n2}")
            s = carry + n1 + n2
            if s > 9:
                ncarry = 1
                s -= 10
            if num3 == "":
                num3 = str(s)
            else:
                num3 = str(s) + num3
            # print(f"c:{carry} + n1:{n1} + n2:{n2} = s:{s} -> nc:{ncarry} => num3:{num3}")
            carry = ncarry
            ncarry = 0
            
        # add carry to num if needed
        if carry != 0:
            num3 = str(carry) + num3
        return num3
                          
        

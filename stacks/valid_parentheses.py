'''
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Stack:
    st = []
    def __init__(self):
        self.st = []

    def push(self, ch):
        self.st.append(ch)
    
    def pop(self):
        if len(self.st):
            return self.st.pop()
    
    def peek(self):
        return self.st[-1]

    def isEmpty(self):
        if len(self.st) == 0:
            return True
        return False
    
    def disp(self):
        print(f"<{self.st}>")

def getMatchingOpenBrace(ch):
    if ch == ')': return '('
    if ch == '}': return '{'
    if ch == ']': return '['
    return None

class Solution:
    def isValid(self, s: str) -> bool:
        st = Stack()
        # st.disp()
        for i in s:
            print(i, end=" ")
            if i in ['(', '[', '{']: 
                st.push(i)
            elif i in [')', ']', '}']:
                # check if tos
                if not st.isEmpty():
                    ch = st.peek()
                    if getMatchingOpenBrace(i) == ch: 
                        # print("pop", end = " ")
                        st.pop()
                    else: # closing brace does not have any match in stack
                        return False
                else: # print("stack empty but we see closing braces")
                    return False
                # st.disp()        
        if st.isEmpty(): # print("all good")
            return True
        return False

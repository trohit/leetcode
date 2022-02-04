'''
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

'''
# oneliner
# return " ".join([i[::-1] for i in s.split()])

class Solution:
    def revWord(self, ss) -> str:
        s = list(ss)
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
            
    def reverseWords(self, s: str) -> str:
        n = len(s)
        revStr = []
        start = 0
        for i in range(n):
            # print(f"{i}:{s[i]}")
            if s[i] == ' ':
                # print(revStr)
                # print(f"will rev [{s[start:i]}]")
                revPart = self.revWord(s[start:i])
                revStr.append(revPart)
                start = i+1
            else:
                pass
        # print(f"finally rev [{s[start:]}]")
        revPart = self.revWord(s[start:])
        revStr.append(revPart)
        res = " ".join(revStr)
        # print(res)
        return res
        
            

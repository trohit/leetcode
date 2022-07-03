"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Runtime: 99 ms, faster than 44.31% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 92.05% of Python3 online submissions for Longest Substring Without Repeating Characters.

Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by left and right.
Space complexity : O(min(m, n)) = O(min(m,n)). Same as the previous approach. We need O(k)O(k) space for the sliding window, where kk is the size of the Set.
The size of the Set is upper bounded by the size of the string nn and the size of the charset/alphabet mm."""
'''
1. keep 2 ptrs left and right, initially both start at 0
2. keep track of how many times each char is seen
3. keep expanding right ptr until it reaches the end of the string
4. keep contracting left ptr and updating stats until dup chars not seen.
5. once no dup chars, at each stage, record the max uniq len seen.
'''
'''
1. keep 2 ptrs left and right, initially both start at 0
2. keep track of how many times each char is seen
3. keep expanding right ptr until it reaches the end of the string
4. keep contracting left ptr and updating stats until dup chars not seen.
5. once no dup chars, at each stage, record the max uniq len seen.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, left, right, max_len = len(s), 0, 0, 0
        chars = [0] * 128    # index where char last seen
        while right < n:
            r = s[right]
            print(f"l:{left} r:{right} [{s[left:right+1]}] max_len:{max_len}")
            chars[ord(r)] += 1
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
                print("contracting left")
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

# *******************************************************
'''
# sub optimal solution put here just for comparison
Runtime: 1241 ms, faster than 5.92% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 13.30% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
def pprint(*args, **kwargs):
    # print("".join( map(str, args) ), **kwargs)
    ...
    
    
class Solution:
    def is_dup(self, c:str, s:str, pos):
        pprint(f"Checking for [{c}] in [{s}]")
        for i in range(len(s)):
            if s[i] == c:
                pprint(f"dup detected at pos {i}->s[i]")
                return i
        return 0
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mlen = 1 # max len seen so far
        dd = {} #dict to store pos of every char
        if len(s) == 0: return 0
        print(s)
        for k,v in enumerate(s):
            print(k, end="")
        print("")
        for k,v in enumerate(s): # loop from 0->n-1
            # del all keys not less than l
            keys = list(dd.keys())
            for kk,vv in enumerate(keys):
                if dd[vv] < l:
                    pprint(f"need to pop {vv}")
                    dd.pop(vv)
                    
            pprint(f"l:{l} k:{k} [{s[l:k+1]}] m:{mlen} d:{dd}")
            if v in dd:
                tlen = k - l # store max len
                pprint(f"dup detected: {v} at pos {dd[v]} tlen:{tlen}")
                l = dd[v] + 1 # shift l to right
                dd[v] = k
            else:
                dd[v] = k
                tlen = k - l + 1
            if tlen > mlen:
                pprint(f"mlen:{mlen}->{tlen}")
                mlen = tlen
        pprint(f"l:{l} k:{k} [{s[l:k+1]}] f({s}):{mlen}")
        return mlen
    
        
"""
****************************************************************

****************************************************************
"""

def pprint(*args, **kwargs):
    ...
    # print("".join(map(str, args)), **kwargs)
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r, mlen = 0, 0, 0 # 2 ptrs l and r
        chars = [0] * 128 # hash table
        while r < n: 
            rch = s[r]
            pprint(f"l:{l} r:{r} [{s[l:r+1]}] max_len:{mlen}", end=" ")
            chars[ord(rch)] += 1
            while chars[ord(rch)] > 1:
                lch = s[l]
                chars[ord(lch)] -= 1
                l += 1
                print("push_l")
            mlen = max(mlen, r-l+1)
            r += 1
            print("push_r")
        return mlen

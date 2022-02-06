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

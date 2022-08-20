"""
https://leetcode.com/problems/group-anagrams
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Runtime: 107 ms, faster than 91.58% of Python3 online submissions for Group Anagrams.
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs List[str]
        :rtype List[List[str]]
        """
        dd = DefaultDict(list)
        for i,ss in enumerate(strs):
            # also works with tuples but a tad slower
            # sss = tuple( ( sorted(ss) ) )            
            sss = "".join( sorted(ss) )
            dd[sss].append(ss)
        print(dd.values())
        return dd.values()
	

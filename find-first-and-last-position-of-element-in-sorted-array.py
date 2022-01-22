'''
L34
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
Runtime: 88 ms, faster than 62.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.5 MB, less than 13.20% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
'''
class Solution:
    def grepl(self, nums, t):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] >= t: # l t m r
                r = m  - 1
            else: # l m t r
                l = m + 1
        if l<0 or l >=n or nums[l] != t:return -1
        return l

    def grepr(self, nums, t):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] <= t:# l m t r
                l = m + 1
            else: # l t m r
                r = m - 1
        if r<0 or r>=n or nums[r] != t:
            return -1
        return r
		    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.grepl(nums, target)
        end = self.grepr(nums, target)
        return [start, end]        

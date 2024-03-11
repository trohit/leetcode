"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dd, n = {}, len(nums)
        # build a freq graph
        for i in nums:
            if i in dd: dd[i] += 1
            else: dd[i] = 1

        # find the num with highest occurences
        maxk, maxv = 0, 0
        for k, v in dd.items():
            if v > n//2: return k

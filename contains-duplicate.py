'''
https://leetcode.com/problems/contains-duplicate/
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

SC: O(n)
TC: O(n)
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n  = len(nums)
        dd = {}
        for i in range(n):
            if nums[i] in dd:
                return True
            else:
                dd[nums[i]] = 1
        return False
        

"""
https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
Easy
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

"""
reader and writer ptr both start at 0 index.
reader goes from 0..n-1
writer overwrites whatever reader reads until 
reader comes across todel 'val' then reader leaves writer behind
T:O(N)
S:O(1)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r, w = 0, 0
        while r < len(nums):
            if nums[r] == val:
                r += 1
            else:
                nums[w] = nums[r]
                w += 1
                r += 1  
        return w  

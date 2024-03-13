"""
https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        a = [0] * len(nums)
        for i in range(len(nums)):
            newpos = (i + k)%n
            # tmp = nums[newpos]
            # print(f"nums[{i}+{k}={newpos}] = {nums[i]}")
            a[newpos] =  nums[i]
        # print(f"{a}")
        nums[:] = a # just copy new arr to result
        

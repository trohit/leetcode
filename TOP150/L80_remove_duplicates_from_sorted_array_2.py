'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
Medium
TC:O(n)
SC:O(1)
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, count = 1, 1
        for p2 in range(1, len(nums)): # iterate with p2 as usual
            if nums[p2] == nums[p2 - 1]:# incr count, until curr elm != prev elm
                count += 1
            else: # reset count if elms are different
                count = 1
            if count <= 2: # if elm seen min twice, then replace elm
                nums[p1] = nums[p2]
                p1 += 1
        return p1

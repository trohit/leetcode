'''
L33
https://leetcode.com/problems/search-in-rotated-sorted-array/
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length),
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Runtime: 69 ms, faster than 16.05% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.8 MB, less than 23.51% of Python3 online submissions for Search in Rotated Sorted Array.
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        xprint(f"binsrc:{nums}")
        n = len(nums)
        l, h = 0, n-1
        while l <= h:
            m = l + ((h - l)//2)
            xprint(f"{l} {m} {h} => {nums[l]} {nums[m]} {nums[h]}", end=" ")
            if nums[m] == target:# straight find
                xprint(f"found at pos:{m}")
                return m
            elif nums[m] >= nums[l]:# mean lt part has no rot
                if target >= nums[l] and target < nums[m]:
                    h=m-1;xprint("<")
                else:
                    l=m+1;xprint(">")
            else: # nums[m] comes equal-to or after rot
                if target > nums[m] and target <= nums[h]:
                    l=m+1;xprint(">>")
                else:
                    h=m-1;xprint("<<")
        return -1

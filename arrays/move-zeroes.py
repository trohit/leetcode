'''
https://leetcode.com/problems/move-zeroes/
283. Move Zeroes Easy
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [1,0,2,0,3,12]
Output: [1,2,3,12,0,0]

Example 3:
Input: nums = [0]
Output: [0]

make a note of 
zero count
keep a ptr to last index where non-0 num needs to be txferred
in loop 1 every non-0 elm is pushed if zero count is seen
in loop 2 all 0s are padded at the end 
SC:O(1)
TC:O(n)
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zc = 0
        ptr = 0
        for i in range(n):
            # xprint(f"{i}->[{nums[i]}] zc={zc} ptr:{ptr}")
            if nums[i] == 0:
                zc = 1
            else: # num != 0, push to front
                if zc != 0:
                    # xprint(f"nums[{ptr}] = {nums[i]}")
                    nums[ptr] = nums[i]
                ptr += 1
        # xprint(f"b4 pad the array with 0s:{nums}")
        while ptr < n:
            # xprint(f"nums[{ptr}] = 0")
            nums[ptr] = 0
            ptr += 1
            
'''
A more elegant approach follows

make a note of 
keep a ptr to last index where non-0 num needs to be txferred
whenever non-0 elm seens, its swapped with ptr 
so 0's get pushed behind
SC:O(1)
TC:O(n)
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptr = 0
        for i in range(n):
            # xprint(f"{i}->[{nums[i]}] ptr:{ptr}")
            if nums[i] != 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

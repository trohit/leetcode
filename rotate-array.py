'''
https://leetcode.com/problems/rotate-array
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Runtime: 216 ms, faster than 84.69% of Python3 online submissions for Rotate Array.
Memory Usage: 25.6 MB, less than 13.87% of Python3 online submissions for Rotate Array.
'''

# simple way to do rotation
'''
every n rotations its back, new_pos = orig_pos
np = i + (k mod n)
'''
class Solution:
    '''
    the simplest way: rotate k times
    SC:O(1)
    TC:O(n)
    ''' 
    def rot_right_by_1(self, nums:List[int]):
        n = len(nums)
        tmp = nums[n-1]
        i = n-1
        while i > 0:
            nums[i] = nums[i-1]
            i -= 1
        nums[0] = tmp
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        SC:O(n)
        TC:O(n)
        """
        n = len(nums)
        onums = [0] * n
        # edge case
        if n == 1:
            return
        for i in range(n):
            npos = (i + (k % n)) % n
            # print(f"f({i}):( {i} + ( {k} % {n} ) % {n} ) = {npos}")
            # print(i, end=":")
            print(onums)
            onums[npos] = nums[i] 
            # self.rot_right_by_1(nums)
        # print(onums)
        for i in range(n):
            nums[i] = onums[i]
            

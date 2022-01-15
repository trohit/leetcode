'''
Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutiv

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

42 / 42 test cases passed.
Status: Accepted
Runtime: 352 ms
Memory Usage: 14.2 MB
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        :type nums List[int]
        :rtype int
        '''
        n = len(nums)
        gmax = 0 
        lmax = 0
        for i in range(n):
            # print(f"i:{i} {nums[i]} lm={lmax} gm:{gmax}")
            if nums[i] == 1:
                lmax += 1
            else: #if nums[i] == 0:
                gmax = max(lmax, gmax)                    
                lmax = 0               
        # if max ones seen till the end
        gmax = max(lmax, gmax)                    
        # print(f"lm={lmax} gm:{gmax}")
        return gmax 
        

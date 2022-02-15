'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''

'''
kadane's algo
also handles empty subarrays
Runtime: 910 ms, faster than 54.05% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28.5 MB, less than 57.88% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = curr_sum = nums[0]
        for i, num in enumerate(nums[1:]):
            curr_sum = max(num, curr_sum + num)
            best_sum = max(best_sum, curr_sum)
            # print(f"n:{num} curr_sum:{curr_sum} best_sum:{best_sum}")
        return best_sum
        

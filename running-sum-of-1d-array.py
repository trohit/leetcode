'''
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
Runtime: 66 ms, faster than 43.89% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.2 MB, less than 26.01% of Python3 online submissions for Running Sum of 1d Array.
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        ll = []
        for i in range(len(nums)):
            s += nums[i]
            ll.append(s)
        return ll

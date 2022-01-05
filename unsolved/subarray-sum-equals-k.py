'''
L560
https://leetcode.com/problems/subarray-sum-equals-k
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
Space:O(1)
Time :O(n*n*n-for-sum) = O(n^3)
61 / 89 test cases passed.
Time Limit Exceeded
"""
def xprint(args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = e = 0
        cnt = 0
        n = len(nums)
        # edge case 
        if n == 1 and k != 1:
            return 0
        for i in range(n):
            for j in range(i+1, n+1):
                xprint(f"{i}..{j} n{nums[i:j]} :{cnt}", end="")
                if sum(nums[i:j]) == k:
                    xprint(" => bump")
                    cnt+=1
                else:
                    xprint("")
        return cnt                    

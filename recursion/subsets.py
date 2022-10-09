"""
https://leetcode.com/problems/subsets
78. Subsets
Medium
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
"""
Approach
As with recursion, two cases need to be handled
1. Base case: leaf node
2. Intermediate managers

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        slate = []
        def dfs(i, lvl = 0):
            print(f"{' '*lvl*2}i:{i} sl:{slate}")
            
            # base case leaf node
            if i >= len(nums):
                print(f"{' '*lvl*2}> adding {slate}")
                res.append(slate.copy())
                return

            # intermediate mgrs
            print(f"{' '*lvl*2}picking up {nums[i]}")
            slate.append(nums[i])
            dfs(i+1, lvl+1)

            # do not pick up
            print(f"{' '*lvl*2}skipping {nums[i]}")
            slate.pop()
            dfs(i+1, lvl+1)
            
        # main
        dfs(0)
        return res
        

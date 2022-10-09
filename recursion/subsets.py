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

This is a problem of subsets(2^n), where each elm could be either present / absent.

As with recursion, two cases need to be handled
1. Base case: leaf node
2. Intermediate managers

Time Complexity:
 = Leaf nodes   + Intermediate/Internal nodes
 = O(2^n) * n/2    O(2^n) * O(1) 
   ^^^^^^^^^^
 = O(2^n)*n
 
Space Complexity: 
   nums          slate             res
 = Input space + Auxiliary space + Output space
 = O(n)          O(n)              O(2^n) * n/2
 = O(2^n)*n
 
Time complexity: O(n*2^n) 
       to generate all subsets and then copy them into output list.
Space complexity: O(N)
       using O(N) space to maintain slate, and are modifying slate in-place with backtracking. 
       Note that for space complexity analysis, we do not count space that is only used for the purpose of returning output, 
       so the output array res is ignored.
       If output arr res is also included, then output arr 'res' space complexity is O(n*2^n). 
 
 https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/
 https://www.geeksforgeeks.org/generating-all-possible-subsequences-using-recursion/
"""

# using recursion and DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        slate = []
        def dfs(i, lvl = 0):
            print(f"{' '*lvl*2}i:{i} sl:{slate}")
            
            # base case leaf node
            if i >= len(nums):
                print(f"{' '*lvl*2}> adding {slate}")
                res.append(slate.copy()) # deep copy as stack unwinding will free slate mem
                return

            # intermediate mgrs
            print(f"{' '*lvl*2}picking up {nums[i]}")
            slate.append(nums[i])
            dfs(i+1, lvl+1)
            # https://stackoverflow.com/questions/67355764/why-do-we-pop-from-the-list-at-the-end-of-each-backtrack-iteration
            slate.pop()  # <<< removing imp else sibling node will pass the extra char to its child nodes and o/p will be longer than expected.    

            # do not pick up
            print(f"{' '*lvl*2}skipping {nums[i]}")
            dfs(i+1, lvl+1)
            
        # main
        dfs(0)
        return res
        

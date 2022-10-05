"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

215. Kth Largest Element in an Array
Medium
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104


Approach:
keep qsel until pivot elem == n -k
each qsel :O(n)
T: in worst case: O(n^2)
T: in practice : O (n log n)
T: actually k log n
so if k much smaller than n
then better than nlogn sorting algos
S: O(1)
"""
import random
def qsel(nums, k, l, r, lvl = 0)->int:
    rand_index = random.randint(l, r)
    nums[rand_index], nums[r] = nums[r], nums[rand_index]
    p, piv = l, nums[r]
    # print(f"partitioning on {piv} l:{l} r:{r}")
    for i in range(l, r):
        # print(f" loop:{nums[l:r+1]} i:{i} p:{p}")
        if nums[i] <= piv:
            # print(f"    swap{i}<>{p}")
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
    # print(f" swap {nums[p]}, {nums[r]}")
    nums[p], nums[r] = nums[r], nums[p]
    # print(f"nums:{nums} p:{p}")
    if p > k:return qsel(nums, k, l, p-1, lvl+1)
    elif p<k:return qsel(nums, k, p+1, r, lvl+1)
    elif p == k:return nums[p] 
    
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # remapping to the index mapping to the kth largest elem
        if len(nums) == 1: return nums[0]
        # print(f"looking for index {k}")
        res = qsel(nums, k, 0, len(nums) - 1)
        # print(f"will be returning {res}")
        return res        

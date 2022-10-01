"""
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
def is_even(num):
    return False if num %2 else True

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        a = nums
        n = len(a)
        l, r = 0, n - 1 
        while l<r:
            # print(f"{a} l:{l} r:{r} {a[l]}<>{a[r]}")
            if is_even(a[l]): l += 1
            if not is_even(a[r]): r -= 1
            if l < r and not is_even(a[l]) and is_even(a[r]):
                # print(f"{a} swap l:{l} r:{r} {a[l]}<>{a[r]}")
                a[l], a[r] = a[r], a[l] # swap l and r nums
        return a   # T:O(n)
        
        
 # simpler soln
 class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
      n = len(A)
      j = 0
      for i in range(n):
          print(f"i:{i} j:{j} a:{A}")
          if A[i] % 2 == 0:
              # print(f"    {A[i]}<>{A[j]}")
              A[i], A[j] = A[j], A[i]
              j += 1
      return A # T:O(n) but faster than opp ptrs due to caching aka locality of reference

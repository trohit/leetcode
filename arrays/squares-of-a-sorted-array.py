'''
https://leetcode.com/problems/squares-of-a-sorted-array/
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Runtime: 360 ms, faster than 26.93% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.6 MB, less than 5.39% of Python3 online submissions for Squares of a Sorted Array.
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def find_first_non_neg(self,nums:List[int], target:int)-> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + ( (r - l) >> 1 )
            xprint(f"{l} {mid} {r}", end=":")
            if nums[mid] > target: # l t m r
                r = mid if mid != r else mid -1
                xprint("<")
            else: # nums[mid] <= target: # l m t r
                xprint(">")                
                l = mid if mid != l else l + 1
        xprint(f"{l} {mid} {r} : found 1st non -ve at {l}")
        return l
                
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # edge case n = 0 , 1
        if n == 0 : return [0]
        elif n == 1: return [nums[0]*nums[0]]
        
        onums = [0] * n
        # first find the first non -ve integer
        r = self.find_first_non_neg(nums, 0)
        
        # have 2 pointers starting from the middle 
        # <----l r--->
        l = r - 1
        k = 0
        while l >= 0 and r < n:
            xprint(onums)
            
            xprint(f"cmp {l} <> {r} : {nums[l]} <> {nums[r]}", end=":")
            if abs(nums[l]) < abs(nums[r]):
                to_swap_pos = l
                l -= 1
                xprint("l")
            else:
                to_swap_pos = r
                r += 1
                xprint("r")
                
            # do in-place swap with k
            xprint(f"onums[{k}] = nums[{to_swap_pos}] -=> {nums[to_swap_pos]}")
            onums[k] = nums[to_swap_pos]* nums[to_swap_pos]
            k += 1

        #[<---l..r]
        while l >= 0:
            xprint(f"l={l} k={k}")
            onums[k] = nums[l]*nums[l]
            l -= 1
            k += 1
        #[l .. r--->]
        while r < n:
            xprint(f"r={r} k={k}")                
            onums[k] = nums[r]*nums[r]
            r += 1
            k += 1
        xprint(onums)
        return onums

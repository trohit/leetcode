'''
L34
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
Runtime: 88 ms, faster than 62.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.5 MB, less than 13.20% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
'''

'''
Explanation
FAQ:
0. how does it work ?
to find the left-most elem, 
1. why is loop condition l<= r and not l<r ?
2. How is the 0 elem / 1 elem case handled ?
3. What if the target elem does not exist in the array ?
 
Rules:
ideally we always want l t r with no m anywhere in between them.
l starts from   0 and only pushes forward if needed.
r starts from n-1 and only pulls back if needed.

get_lmost: here we want l to slide left until we get the 1st lmost elem 
case 1:  
if mid elem m >= t, then it could be shown as : 
l t m r
	then r feels m is between itself and t 
	then r pulls back and jumps over m to get closer to t.
	=> r = m - 1
	
case 2:
else if mid elem m < t, then can be represented as :
l m t r 
	then l feels m is between itself and t 
	then l jumps over m to get closer to t. 
	=> l = m + 1

Simulation:
nums:[5, 7, 7, 8, 8, 10]
target = 6
[  5 ,  7 ,( 7),  8 ,  8 , 10] ,
   l   t     m              r
   0         2              5
sl:0 2 5 => a[2]:7:<

[( 5),  7] ,  7 ,  8 ,  8 , 10 ,
  l|m t r 
sl:0 0 1 => a[0]:5:>

  5 ,[( 7)],  7 ,  8 ,  8 , 10 ,
     lt mr
sl:1 1 1 => a[1]:7:<

  5 ,[( 7)],  7 ,  8 ,  8 , 10 ,
  r  t  l
<<sl:1 1 0 => a[1]:7:
in the end, l and r swap
as 't' may not even be in the arr, a last check is needed to see is nums[l] != target, 
in which case -1 is returned.

While doing get_lmost
in the end, l and r has swapped positions as we loop until l <= r, 
so aray would be [ ...r l... ]
                        t t 
So we return l as 1st or lmost elm



[  5 ,  7 ,( 7),  8 ,  8 , 10] ,
   l  t      m              r
HI:0 2 5 => a[2]:7:<

[( 5),  7] ,  7 ,  8 ,  8 , 10 ,
  lm  t r 
HI:0 0 1 => a[0]:5:>

  5 ,[( 7]),  7 ,  8 ,  8 , 10 ,
     lt mr
HI:1 1 1 => a[1]:7:<

  5 ,[( 7]),  7 ,  8 ,  8 , 10 ,
  r  t  m l   
>>sr:1 1 0 => a[1]:7:
in the end, l and r swap and become r,l.
Here 'r' becomes the rightmost elem.
as 't' may not even be in the arr, a last check is needed to see is nums[r] != target, 
in which case -1 is returned.

While doing get_rmost:
in the end, l and r has swapped positions as we loop until l <= r, 
so aray would be [ ...r l... ]
                    t t
So we return r as last or rmost elm

																						  
get_rmost: here we want r to slide right until we get the last rmost elem
case 1:  
if mid elem m <= t, then it could be shown as : 
l m t r 
	then l feels m is between itself and t 
	then l jumps over m to get closer to t. 
	=> l = m + 1

case 2:
if mid elem m > t, then it could be shown as : 
l t m r 
	then r feels m is between itself and t 
	then r pulls back and jumps over m to get closer to t.
	=> r = m  - 1


'''
class Solution:
    def grepl(self, nums, t):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] >= t: # l t m r
                r = m  - 1
            else: # l m t r
                l = m + 1
        if l<0 or l >=n or nums[l] != t:return -1
        return l

    def grepr(self, nums, t):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] <= t:# l m t r
                l = m + 1
            else: # l t m r
                r = m - 1
        if r<0 or r>=n or nums[r] != t:
            return -1
        return r
		    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.grepl(nums, target)
        end = self.grepr(nums, target)
        return [start, end]        

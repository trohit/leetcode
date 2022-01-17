'''
L34
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

Find First and Last Position of Element in Sorted Array
Medium
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Runtime: 169 ms, faster than 5.19% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 16.2 MB, less than 12.84% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
'''
import bisect
def xprint(*args, **kwargs):
    # return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        xprint(f"nums:{nums}")
        n = len(nums)
        l, h = 0, n-1
        ss = set()
        # corner case len 0 and 1
        if n == 0:
            return [-1,-1]
        elif n ==1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
                
        while l < h:
            m = l+((h-l)>>1)
            xprint(f"{l} {m} {h} => a[{m}]:{nums[m]} ss:{ss}")
            if nums[m] == target:
                # xprint(f"store pos {m}")
                # ss.add(m)
                if m!=0 and m != n-1 and nums[m-1] == nums[m] and nums[m] == nums[m+1]: 
                    xprint(f"add both {m-1} & {m+1}")
                    ss1 = self.searchRange(nums[:m], target)
                    ss2 = self.searchRange(nums[m:], target)
                    xprint(f"s1:{nums[:m]}")
                    xprint(ss1)
                    ss2 = set([x+m for x in ss2])
                    xprint(f"s2:{nums[m+1:]}")
                    xprint(ss2)
                    ss = ss.union(ss1, ss2)
                    break
                elif m != n-1 and nums[m] == nums[m+1]:
                    # if the rt neigh is same num, search l
                    ss.add(m+1)
                    xprint(f"add rt {m+1}")
                    l=m+1
                elif m != 0 and nums[m-1] == nums[m]: 
                    # if the lt neigh is same num, search r
                    ss.add(m-1)
                    xprint(f"add lt {m-1}")
                    h=m-1
                else: 
                    xprint("neither l nor r dups")
                    break
                    
            elif nums[m] <= target:
                xprint(">")
                l=m+1
            else:
                xprint("<")                
                h=m-1
        # if l == r and elm sits here
        if l == h and nums[l] == target:
            xprint(f"adding {l}")
            ss.add(l)
        if len(ss):
            ll = sorted(list(ss))
            xprint(f'll:{ll}')
            return [ll[0], ll[-1]]
        else:
            return (-1,-1)
                
        

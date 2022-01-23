'''
https://leetcode.com/problems/single-element-in-a-sorted-array
L540
540. Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10


Logic:
1. to keep things simple, we slide mid to the right most dup.
2. We know that if no single elems exists, right most dup must be at an odd numbered index.
[1,1,2,2]
 0 1 2 3
3. We know that if a single elem exists, right most dup must be at an even numbered index.
[0,1,1,2,2]
 0 1 2 3 4
4. So at every bisect, push mid until its at the 2nd dup elem, then if even there is a single elems to its left, else search right.
5. When shrinking the window and moving left, no need to consider mid and mid-1 in the next search.
6. When shrinking the window and moving right, no need to consider any elems upto mid in the next search.

Runtime: 172 ms, faster than 67.41% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 24.3 MB, less than 66.18% of Python3 online submissions for Single Element in a Sorted Array.
'''
def xprint(*args, **kwargs):
    return
    print("". join(map(str, args)), **kwargs)
    
    
def showarr(a, l, m, r):
    n = len(a)
    for i in range(n):
        # start
        if i == l:
            print(f"[", end="")
        if i == m:
            print(f"(", end="")
        else:
            print(f" ", end="")
        # mid
        print(f"{a[i]:>2}", end="")
        # end
        if i == r:
            print(f"]", end="")
        if i == m:
            print(f")", end="")
        else:
            print(f" ", end="")
        print(",", end="")
    print("")
        

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n %2 == 0:
            print(f"no odd elems")
            return 1
        l, r = 0, n - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == nums[mid + 1]:
                xprint(f"rt shift {mid} as {nums[mid]} at {nums[mid+1]}")
                mid = mid + 1
            # showarr(nums, l, mid, r)
            xprint(f"{l} {mid} {r} => {nums[mid]=}", end=":")
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid + 1]:
                xprint(f"found {mid}")
                return nums[mid]
            elif (mid) % 2 == 0:# odd # of occurences on the left
                r = mid - 2
                xprint("<")
            else: # search right
                l = mid + 1
                xprint(">")
        xprint(f"END:{l} {r}", end=":")
        return nums[l]
                
            
        

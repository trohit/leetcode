"""
L88: Merge Sorted array
https://leetcode.com/problems/merge-sorted-array/

https://www.youtube.com/watch?v=P1Ic85RarKY
Naive solution: copy nums2 elms into the 2nd part of nums1 and simple sort. T:O(n+m)log(n+m)
OptB: copy non-0 elms of nums1 -> another arr cp_nums1 and merge(cp_nums1, nums2) into nums1. 
    T:O(n)+O(n+m) but space needed is O(n+m)
OptC: to optimize space, use 3ptrs: variation of 2 ptrs pattern and start filling nums1 from largest to smallest
    a 3rd ptr di(dst index) -> from range(m+n to n, -1)
    T: O(m+n) S:O(m+n) 
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        di = m+n-1 # both indexes
        while m and n:
            if nums1[m-1] > nums2[n-1]: 
                nums1[di] = nums1[m - 1]
                m -= 1
            else: # move all elms one to the right
                nums1[di] = nums2[n-1]
                n -= 1
            di-=1

        # copy any remaining leftover elms from nums2 -> nums1
        while n:
            nums1[di] = nums2[n-1]
            n, di = n-1, di-1 
        

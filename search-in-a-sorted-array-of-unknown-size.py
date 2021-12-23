# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
'''
702. Search in a Sorted Array of Unknown Size
This is an interactive problem.

You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
returns 231 - 1 if the i is out of the boundary of the array.
You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: secret = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in secret and its index is 4.
Example 2:

Input: secret = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in secret so return -1.
 

Constraints:

1 <= secret.length <= 104
-104 <= secret[i], target <= 104
secret is sorted in a strictly increasing order.
'''

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        """
        will assume that 2147483647 is out of arr bounds
        so valid index from 0..2^^31-2 
        """
        st = 0
        end = (2**31) -2
        while st <= end:
            mid = st + ((end - st)//2)
            if reader.get(mid) > target:
                end = mid - 1
            elif reader.get(mid) < target:
                st = mid + 1
            elif reader.get(mid) == target:
                return mid
        return -1
       
       
# faster way => 40ms -> 36ms

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        """
        so valid index from 0..2^^31-2
        
        valid max index : 10**4 = 
        10001
        2147483647
        """
        BAD_VAL = (2**31)-1
        st = 0
        end = 2
        # faster way to compute upper limit using exponential gallop i.e. power of 2
        while reader.get(end) != BAD_VAL:
            end*=2
        while st <= end:
            mid = st + ((end - st)//2)
            if reader.get(mid) > target:
                end = mid - 1
            elif reader.get(mid) < target:
                st = mid + 1
            elif reader.get(mid) == target:
                return mid
        return -1

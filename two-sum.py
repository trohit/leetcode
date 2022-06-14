'''
L1
https://leetcode.com/problems/two-sum/
Space: O(n)
Time : O(n)
Runtime: 48 ms, faster than 99.25% of Python3 online submissions for Two Sum.
Memory Usage: 15.4 MB, less than 41.58% of Python3 online submissions for Two Sum.

'''
def xprint(*args, **kwargs):
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        :type nums list
        :type target int
        :rtype list
        '''
        dd = dict()
        for i,v in enumerate(nums):
            buddy_val = target - v
            if buddy_val in dd:
                return [i,dd[buddy_val]]
            dd[v] = i #store pos of the value
        

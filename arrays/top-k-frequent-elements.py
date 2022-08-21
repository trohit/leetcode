'''
https://leetcode.com/problems/top-k-frequent-elements/
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2], k = 2
Output: [1,2]

Runtime: 143 ms, faster than 67.73% of Python3 online submissions for Top K Frequent Elements.
'''

from collections import defaultdict 
class Solution:
    def get_first_k_elems(self, ll:list, k:int):
        ll = sorted(ll, reverse = True)
        freq_ll = [n for (f,n) in ll]
        # print(f"sorted ll:{ll}")
        # print(f"sorted freq_ll:{freq_ll}")
        return freq_ll[:k]
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums List[int]
        :type k int
        :rtype List[int]
        """
        sorted_k_keys = []
        dd = defaultdict(int)
        for i,v in enumerate(nums):
            dd[v] += 1
        ll = [] # list of tuples [(freq1, num1), (freq2, num2),..]
        for num in (dd):
            # print(f"num:{num}")
            freq = dd[num]
            tup = (freq, num)
            ll.append(tup)
        
        # print(f"dd {{num1:freq1, ...}}:{dd}")
        # print(f"ll[f1,n1,...]:{ll}")
        elms_ll = self.get_first_k_elems(ll, k)
        # print(f"sorted_k_keys:{sorted_k_keys}")
        return elms_ll

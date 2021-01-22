# https://leetcode.com/problems/top-k-frequent-elements/
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        # build a dict of num, freq mappings
        c = dict(Counter(nums))
        
        return heapq.nlargest(k, c.keys(), key=c.get)

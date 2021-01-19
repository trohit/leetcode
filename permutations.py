# https://leetcode.com/problems/permutations/
"""
Runtime: 40 ms, faster than 71.01% of Python3 online submissions for Permutations.
Memory Usage: 14.4 MB, less than 73.44% of Python3 online submissions for Permutations.
time:O(n!)
space:O(n!)
"""
class Solution:
    seq = []
    def __init__(self):
        self.seq = []
        
    def perm(self, a, i = 0):
        n = len(a)
        if i == n:
            self.seq.append(list(a))
        else:
            for j in range(i,n):
                if i != j:
                   a[i], a[j] = a[j], a[i]
                self.perm(a,i+1)
                if i != j:
                    a[i], a[j] = a[j], a[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.perm(nums)
        return(self.seq)
        

'''
L1570
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/submissions/
Runtime: 1668 ms, faster than 99.82% of Python3 online submissions for Dot Product of Two Sparse Vectors.
Memory Usage: 18.2 MB, less than 87.02% of Python3 online submissions for Dot Product of Two Sparse Vectors.
'''
class SparseVector:
    ll1 = []
    def __init__(self, nums: List[int]):
        self.ll1 = nums
    
    def __len__(self):
        return len(self.ll1)
    
    def __getitem__(self, i):
        return self.ll1[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ll2 = vec
        prod = 0
        max_len = max(len(self.ll1), len(vec))
        for i in range(max_len):
            if self.ll1[i] == 0 or ll2[i] == 0:
                continue
            else:
                prod += (self.ll1[i] *ll2[i])
        return prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

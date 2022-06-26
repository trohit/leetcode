"""
https://leetcode.com/problems/random-pick-with-weight
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[10,7,8,10]],[],[],[],[],[]]
Runtime: 8620 ms, faster than 5.01% of Python3 online submissions for Random Pick with Weight.
Memory Usage: 19.7 MB, less than 6.93% of Python3 online submissions for Random Pick with Weight.

time : O(n)
space: O(n)

"""
import random
class Solution:
    ws = hv = []
    def __init__(self, w: List[int]):
        self.ws = w.copy()
        self.hv = self.compute_hi_vals(w)
        print(self.hv)
        
    def compute_hi_vals(self, w):
        tot = sum(w)
        ll = []
        for i in range(len(w)):
            watermark = ((w[i] / tot) * 100)
            if i > 0:
                watermark += ll[i-1]
            # print(f"appending {watermark}")
            ll.append(watermark)
        return ll

    def pickIndex(self) -> int:
        r = random.randrange(1,100)
        print(r)
        for i in range(len(self.hv)):
            if r <= self.hv[i]:
                
'''
*********************
# bit faster approach
*********************
Runtime: 7944 ms, faster than 8.04% of Python3 online submissions for Random Pick with Weight.
Memory Usage: 18.9 MB, less than 12.76% of Python3 online submissions for Random Pick with Weight.
'''
class Solution:

    def __init__(self, w: List[int]):
        # make weights
        self.parr = [x/sum(w) for x in w]

        # make absolute vals in l
        self.l = [0]*len(self.parr)
        prev_sum = 0
        for k,v in enumerate(self.parr):
            self.l[k] = prev_sum + self.parr[k]
            prev_sum = self.l[k]
        
    def pickIndex(self) -> int:
        rnd = random.random()
        # chek for 1st index that is less than or equal to values in abs arr l
        for k,v in enumerate(self.l):
            if rnd <= self.l[k]:
                return k

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
                return i
        print("something bad hapened")
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

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
        

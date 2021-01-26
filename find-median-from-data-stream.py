"""
https://leetcode.com/problems/find-median-from-data-stream
Runtime: 1424 ms, faster than 7.66% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 25.7 MB, less than 42.30% of Python3 online submissions for Find Median from Data Stream.

Time Submitted Status Runtime Memory Language
01/26/2021 23:32	Accepted	1424 ms	25.7 MB	python3

time:O(nlogn(+n)) = O(nlogn)
space:O(n)
"""
class MedianFinder:
    cnt = 0
    ll = []
    tot = 0
    def __init__(self):
        self.cnt = 0
        self.ll = []
        self.tot = 0

    def addNum(self, num: int) -> None:
        self.cnt+=1
        self.tot+=num
        self.ll.append(num)
        
    def findMedian(self) -> float:
        medval = 0
        midpos = self.cnt//2
        self.ll.sort()
        # print(f"{self.ll} {self.cnt}")

        # edge cases
        if self.cnt == 0:
            self.medval = 0
        elif self.cnt == 1:
            medval = self.tot
        elif self.cnt %2 != 0: #odd
            medval = self.ll[midpos]
        else: # even
            midpos-=1
            medlo = self.ll[midpos]
            medhi = self.ll[midpos+1]
            medval = (medlo+medhi)/2.0
        # print(f"midpos:{midpos} med:{medval}")
        return medval

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

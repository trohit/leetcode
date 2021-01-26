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

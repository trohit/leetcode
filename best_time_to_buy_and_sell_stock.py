# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Input: prices = [7,1,5,3,6,4]
# Output: 5
"""
T: O(n)
S: O(1)
https://www.youtube.com/watch?v=1pkOgXD63yU
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        a = prices
        max_prof = 0
        l, r = 0, 1
        while r < n:
            t_prof = a[r] - a[l] 
            # print(f"{t_prof} = a[{r}] - a[{l}]")
            if t_prof < 0: l = r
            else: max_prof = max(t_prof, max_prof)
            r+=1
        return max_prof

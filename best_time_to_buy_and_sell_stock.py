# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Input: prices = [7,1,5,3,6,4]
# Output: 5
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = max(0, prices[1] - prices[0])
        min_price = prices[0]
        for p in prices[1:]:
            max_profit = max(p - min_price, max_profit)
            min_price = min(p, min_price)
        return max_profit
        

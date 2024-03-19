"""
122. Best Time to Buy and Sell Stock II
Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""
"""
T:O(n) S:O(1)
have 2 ptrs
bp and sp
sp keeps moving unconditionally
bp moves only when bp > sp
at each step, calculate profit
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        valley, peak, profit = 0, 0, 0
        while peak < len(prices):
            # print(f"v:{valley} p:{peak} p:{profit}")
            if prices[peak] < prices[valley]:
                valley = peak # if lower minima found jump to it
            diff = prices[peak] - prices[valley]
            if diff > 0:
                profit += diff
                valley = peak # move valley as the profit until this point is already calculated
            peak += 1
        # print("All done")
        return profit

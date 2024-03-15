"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

T:O(n)
S:O(1)
"""
"""
use 2 ptrs, where 
bp -> buy ptr: best buy day
sp -> sell ptr: best sell day
sp > bp as buy and sell day have to be different

sp iterates from [1..n]
if bp > sp : then we d
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bd : bbd : best buy day
        # sd : bsd : best sell day
        bd, sd = 0, 1
        profit = 0
        # print(f"prices:{prices}")
        while sd < len(prices):
            diff = prices[sd] - prices[bd]
            # print(f"bd:{bd} sd:{sd} {prices[sd]}-{prices[bd]}:{diff} profit:{profit}")
            if diff > profit: # store the best profit
                profit = diff
            if prices[sd] < prices[bd]: # found a lower minima
                bd = sd #  move bp to this new minima
            sd += 1 # sp iterates from begin..end
        return profit
        

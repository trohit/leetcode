'''
322. Coin Change
https://leetcode.com/problems/coin-change/
You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
'''

# non -working doluton, working solution needs bfs or dynamic programming
debug_lvl = -1 # default debug level, to suppress all output set to -1
def dprint(verbosity_lvl, *args, **kwargs):
    if debug_lvl >= verbosity_lvl:
        print(f">" * verbosity_lvl, end="")
        print("".join(map(str, args) ), **kwargs)
    return
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = 0
        dprint(0, f"coins:{coins} amt:{amount}")
        while amount:
            dprint(1, f"amt left: {amount} num_coins:{num_coins}")
            for i in range(len(coins)-1, -1, -1):
                dprint(3, f"examining {coins[i]}")
                if amount >= coins[i]:
                    dprint(2, f"computing: {amount} - {coins[i]}")
                    amount -= coins[i]
                    num_coins += 1
                    break
                else:
                    dprint(0, "no coins match, returning -1")
                    return -1
                    # continue
        dprint(0, f"num_coins:{num_coins}")
        return num_coins

    
'''
Classy explanation to the prob here:
https://www.youtube.com/watch?v=H9bfqozjoqs&t=3s

Details 
Runtime: 1620 ms, faster than 72.17% of Python3 online submissions for Coin Change.
Memory Usage: 14.3 MB, less than 47.58% of Python3 online submissions for Coin Change.
'''
class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        dp = [amount+1]*(amount + 1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    tmp = min(dp[a], 1 + dp[a-c])
                    dp[a] = tmp
        return dp[amount] if dp[amount] != amount + 1 else -1

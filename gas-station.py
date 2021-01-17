# https://leetcode.com/problems/gas-station/
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Runtime: 3888 ms, faster than 12.69% of Python3 online submissions for Gas Station.
# Memory Usage: 15.2 MB, less than 30.24% of Python3 online submissions for Gas Station.
class Solution:
    def simtrip(self, gas, cost, si)-> bool:
        g = 0
        i = si
        n = len(gas)
        is_starting = True
        while True:
            if i == si and is_starting == False:
                # print("Feasible")
                return True
            is_starting = False
            fg = g + gas[i] #fill 'er up
            rg = fg - cost[i] # burn to get o the next town
            if rg < 0:
                # print(f"ran out of fuel at {si}")
                return False
            # print(f"Travel to station {i}. Your tank = {g} + {gas[i]} - {cost[i]}  = {rg}")
            g = rg
            # go to next station
            i = i+1
            if i == n:
                i = 0
        return False

            
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(0, n):
            # print(f"starting at stn {i} and filling up {gas[i]} units of gas")
            res = self.simtrip(gas, cost, i)
            if res == True:
                return i
        return -1

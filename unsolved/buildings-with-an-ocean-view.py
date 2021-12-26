'''
L1762
https://leetcode.com/problems/buildings-with-an-ocean-view/

Runtime: 836 ms, faster than 17.94% of Python3 online submissions for Buildings With an Ocean View.
Memory Usage: 32.1 MB, less than 7.65% of Python3 online submissions for Buildings With an Ocean View.

Constraints
1. output in incresing index order

Examples
Ranges
Observations/ Rules
1. right most building can always see
2. A bldg can only see the ocean if its greater than all its right most neighbors.

Testcases
1. None can see (except rt most)
2. All can see
3. Some can see(rt most + some others)

Algo/Approach
Brute force
Optimizations

Complexity
Time : O(len=>n + loop=>n + append=>1 + assign =>1 + reverse(n)) = 2.5n ~ O(n)
Space
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_so_far = 0
        can_see_ll = []
        n = len(heights)
        for i in range(n-1, -1, -1): # search from right to left
            xprint(f"i:{i} msf:{max_so_far}")
            if heights[i]> max_so_far:
                can_see_ll.append(i)
                max_so_far = heights[i] # new max height
        # reverse result
        return can_see_ll[::-1]

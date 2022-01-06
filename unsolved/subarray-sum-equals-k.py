'''
L560
https://leetcode.com/problems/subarray-sum-equals-k
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
Space:O(1)
Time :O(n*n*n-for-sum) = O(n^3)
61 / 89 test cases passed.
Time Limit Exceeded

See:
https://leetcode.com/problems/subarray-sum-equals-k/discuss/503178/Python5-Approaches-easy-to-understand-with-detailed-explanations
"""
def xprint(args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = e = 0
        cnt = 0
        n = len(nums)
        # edge case 
        if n == 1 and k != 1:
            return 0
        for i in range(n):
            for j in range(i+1, n+1):
                xprint(f"{i}..{j} n{nums[i:j]} :{cnt}", end="")
                if sum(nums[i:j]) == k:
                    xprint(" => bump")
                    cnt+=1
                else:
                    xprint("")
        return cnt                    
'''
Approach - 2
Time Limit Exceeded
61 / 89 test cases passed.
Space: O(n)
Time : O(n^2)
'''
def xprint(args, **kwargs):
    # return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sll = [0] * (n+1)
        cnt = 0
        # store all the sums
        for i in range(1, n+1):
            sll[i] = sll[i - 1] + nums[i - 1]
        # print(sll)
        
        for start in range(n):
            xprint("")
            for end in range(start+1, n+1):
                xprint(f"{start}..{end} {sll[start:end+1]} ({sll[end]}-{sll[start]}) sum:{sll[end] - sll[start]} :{cnt}", end="")
                if sll[end] - sll[start] == k:
                    xprint(" => bump")
                    cnt += 1
                else:
                    xprint("")
        return cnt
            
'''
Approach - 3
Keep start at one place.
keep adding to sum as end pointers loops around.
Space: O(1)
Time : O(n^2)
Time Limit Exceeded
61 / 89 test cases passed.

'''
def xprint(args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        # store all the sums
        
        for start in range(n):
            s = 0
            xprint("")
            for end in range(start, n):
                xprint(f"{start}..{end} {nums[start:end+1]} :{cnt}", end="")
                s += nums[end]
                if s == k:
                    xprint(" => bump")
                    cnt += 1
                else:
                    xprint("")
        return cnt
             

"""
39. Combination Sum
Medium
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
 
Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

"""

"""
"""
Approach:
DFS based solution that uses backtracking
T:O(n^(T/M)) where T is tgt vale and M is the minimal val in the arr
    height of n-ary tree is T/M
At each node, it takes a constant time to process, except the leaf nodes which could take a linear time to make a copy of combination.
So we can say that the time complexity is linear to the number of nodes of the execution tree.
First of all, the fan-out of each node would be bounded to NN, i.e. the total number of candidates.
The maximal depth of the tree, would be T/M, where we keep on adding the smallest element to the combination.
As we know, the maximal number of nodes in N-ary tree of T/M height would be n^{T/M+1} 

S:O(T/M) 
We implement the algorithm in recursion, which consumes some additional memory in the function call stack.

number of recursive calls can pile up to T/M, where we keep on adding the smallest element to the combination. As a result, the space overhead of the recursion is O(T/M)

Note that, we did not take into the account the space used to hold the final results for the space complexity.
If we account the space used for output, then it becomes:  
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bt(rem, i, sl, res):
            # base case
            if rem == 0: 
                res.append(list(sl)                   # make a deep copy of the current combination
                return
            
            if rem < 0: return                        # exceed the scope, stop exploration.
            
            # nested lazy mgr case
            for j in range(i, len(candidates)):
                sl.append(candidates[j])              # add the number into the combination
                bt(rem - candidates[j], j,  sl, res)  # give the current number another chance, rather than moving on
                sl.pop()                              # backtrack, remove the number from the combination
                
        res = []
        bt(target, 0, [], res)
        return res            

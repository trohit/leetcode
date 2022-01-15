# https://leetcode.com/problems/binary-search
'''
Simple to grasp the concept but notoriously hard to get right
https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
https://stackoverflow.com/questions/6372037/binary-search-problems
https://www.geeksforgeeks.org/problem-binary-search-implementations/

The one template for all binary search algos
https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        si = 0
        ei = len(nums) -1
        while si <= ei:
            mi = si + (ei-si)//2
            xprint(f"{target} {si} {mi} {ei}")
            if nums[mi] > target:
                ei = mi-1
            elif nums[mi] < target:
                si=mi+1
            elif nums[mi] == target:
                return mi
            else:
                return mi+1
        return -1
        

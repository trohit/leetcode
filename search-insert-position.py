'''
L35
35. Search Insert Position
Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Runtime: 52 ms, faster than 59.13% of Python3 online submissions for Search Insert Position.
Memory Usage: 15 MB, less than 56.36% of Python3 online submissions for Search Insert Position.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1
        while l <= r: 
            '''
            needs to be '<=' instead of just '<' 
            as the num may not be int list
            and then we need to return just the 
            pos of the elm where it should be inserted.
            '''
            mid = l+ ( (r-l)>>1 )
            print(f"{l}..{mid}..{r}")
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                print(f"l = {mid}+1")
                l = mid + 1
            else: #mid > target
                r = mid - 1
                print(f"r = {mid}-1")
            print(f"returning {l}")
        return l
        

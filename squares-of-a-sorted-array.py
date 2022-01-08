'''
L977
https://leetcode.com/problems/squares-of-a-sorted-array/
Runtime: 232 ms, faster than 63.90% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.4 MB, less than 5.48% of Python3 online submissions for Squares of a Sorted Array.

977. Squares of a Sorted Array (Easy)
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''
'''
have 2 ptrs p1 and p2
[-4,-1,0,3,10]
     ^ ^
<--- p1p2-->
merge the two arrays and square them as you go

'''
def xprint(*args, **kwargs):
    # return
    print("".join(map(str, args)), **kwargs)
    
# p1 points to index of last -ve num
def find_p1(nums):
    xprint(nums)
    lo = 0
    n = len(nums)
    hi = n-1
    # case 0: last num in arr is -ve
    if nums[hi] < 0:
        return hi
    # case 1: 1st num in arr is non -ve
    if nums[lo] > 0:
        return lo-1
    
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        xprint(f"{lo}..{mid}..{hi}")
        if nums[mid] > 0:
            xprint("<")
            hi = mid - 1
        elif nums[mid] < 0:
            xprint(">")
            lo = mid + 1
        elif nums[mid] == 0:
            xprint("=")
            mid -=1
            return mid
    # handle 2nd last cases, where 2nd last num is -ve or 2nd num is +ve
    # case 1: the last -ve number
    if nums[mid] < 0 and nums[mid+1] >= 0:
        pass
    # case 2: the first non -ve number
    elif nums[mid] > 0 and nums[mid-1] < 0:
        mid -= 1
    xprint(f"over {lo}..{mid}..{hi}")
    return mid
        

def show_arr(nums, p1, p2):
    for i,v in enumerate(nums):
        if i == p1:
            xprint(f"({v})",end=",")
        elif i == p2:
            print(f"{{{v}}}",end=",")
        else:
            xprint(f"{v}",end=",")
    xprint('')
            
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        p1 = len(nums)-1 # index of last -ve num
        p2 = len(nums)   # index of 1st non -ve num
        p1 = find_p1(nums)
        p2 = p1+1
        xprint(p1)
        '''
        # slower than bin search to find p1
        for i in range(len(nums)):
            # xprint(f"i:{i} => {nums[i]}")
            if nums[i] >= 0:
                p2 = i
                p1 = i-1
                break
        # show_arr(nums,p1,p2)
        '''
        xprint(f"p1:{p1} p2:{p2} {nums[:p1+1]}{nums[p2:]} ")
        # merge the two arrays
        while p1 >= 0 and p2 < len(nums):
            c1 = nums[p1]*nums[p1]
            c2 = nums[p2]*nums[p2]
            if c1 > c2:
                ch = c2
                res.append(ch)
                p2+=1
            else:
                ch = c1
                res.append(ch)
                p1-=1
            # xprint(f"p1:{p1} p2:{p2} {c1}<>{c2} {res}")
            
        # case 1 : len(p1) > len(p2)
        if p1 > -1:
            l1 = [i**2 for i in nums[p1::-1]]
            # xprint(f"l1 {p1} remnant: {l1}")
            res.extend(l1)
        
        # case 2 : len(p2) > len(p1)
        if p2 < len(nums):
            l2 = [i**2 for i in nums[p2:]]
            # xprint(f"l2 remnant: {p2} {l2}")
            res.extend(([x**2 for x in nums[p2:]]))
        return res
        

'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
SC: O(1)
TC: O(n)

Runtime: 76 ms, faster than 55.54% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.7 MB, less than 59.59% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
'''
def xprint(*args, **kwargs):
    return
    print("".join( map(str, args) ), **kwargs)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return self.brueforce(numbers, target)
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            xprint(f"checking if {l}+{r} => {numbers[l]} + {numbers[r]}")
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target: 
                l += 1
            else:
                r -= 1
        
    def brueforce(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            j = i + 1
            while j < n:
                xprint(f"checking if {i}+{j} => {numbers[i]} + {numbers[j]}")
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                j = j + 1
        return [-1, -1]
        

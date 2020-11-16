#  Remove Duplicates from Sorted Array
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

cp:0 lp:1 gt:1
               1 1 2 2 3 3 4 
cp:1 lp:1 gt:1
               1 1 2 2 3 3 4 
cp:2 lp:1 gt:1
               1 1 2 2 3 3 4 swap bet [1]1 <> [2]2
cp:3 lp:2 gt:2
               1 2 1 2 3 3 4 
cp:4 lp:2 gt:2
               1 2 1 2 3 3 4 swap bet [2]1 <> [4]3
cp:5 lp:3 gt:3
               1 2 3 2 1 3 4 
cp:6 lp:3 gt:3
               1 2 3 2 1 3 4 swap bet [3]2 <> [6]4
               1 2 3 4 
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        gt = nums[0]
        lp = 1
        for cp,v in enumerate(nums):
            print("cp:{} lp:{} gt:{}".format(cp, lp, gt))
            #dispList(nums)
            if v > gt:
                #print("swap bet [{}]{} <> [{}]{}".format(lp, nums[lp], cp, v))
                # swap pos
                tmp = nums[lp]
                nums[lp] = nums[cp]
                nums[cp] = tmp
                lp+=1
                gt = v
        return lp
"""
  
def rmDups(nums: list) -> int:
    gt = nums[0]
    lp = 1
    for cp,v in enumerate(nums):
        print("cp:{} lp:{} gt:{}".format(cp, lp, gt))
        dispList(nums)
        if v > gt:
            print("swap bet [{}]{} <> [{}]{}".format(lp, nums[lp], cp, v))
            # swap pos
            tmp = nums[lp]
            nums[lp] = nums[cp]
            nums[cp] = tmp
            lp+=1
            gt = v
        else:
            print("")
    return lp
    
# driver
#main
nums = [1,1,2,2,3,3,4]
# print(Solution.removeDuplicates(nums))
res = rmDups(nums)
dispList(nums, res)
        

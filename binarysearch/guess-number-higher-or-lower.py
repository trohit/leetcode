'''
https://leetcode.com/problems/guess-number-higher-or-lower

374. Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Runtime: 48 ms, faster than 30.93% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14 MB, less than 13.12% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        while l <= h:
            m = l + (( h - l ) >> 1)
            # print(f"guessed {m}")
            g = guess(m)
            if  g == -1:
                h = m - 1
            elif g == 1:
                l = m + 1
            else:
                return m
        print(f"{n} not found")
        

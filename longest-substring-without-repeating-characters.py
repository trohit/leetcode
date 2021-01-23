"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Runtime: 672 ms
Memory Usage: 14.4 MB

Time: O(n) as if all the elements are the same, and the string len is 100, pgm will examine all 100 elems with some elems being examined again 
Space: O(k) where k is the number of unique elems in the stringand in worst case k=n 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mlen=cnt=i=0
        ss=dict()
        while i < len(s):
            #print(f"{i} {s[i]} {mlen}")
            if s[i] not in ss:
                ss[s[i]]=i
                cnt+=1
                i+=1
            else:
                #print("dup")
                if mlen<cnt:
                    mlen=cnt
                    #print(f"newm:{mlen}")
                
                oldpos=ss[s[i]]
                ss.clear()
                #ss[s[i]]=i
                cnt=0
                i=oldpos+1
            #print(f"{s[i]} {cnt}")
        #print(f"{mlen} {cnt}")
        mlen=max(mlen,cnt)
        return mlen
            
        

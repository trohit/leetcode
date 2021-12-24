'''
L438
https://leetcode.com/problems/find-all-anagrams-in-a-string/
time exceeded 33/61 cases
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)

import collections
def get_hist(s):
    hist = collections.defaultdict(int)
    for i in s:
        hist[i]+=1
    return hist
        
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = set() # {} but for set not dict
        xprint(f"searching for {p} in {s}")
        for i in range(0, len(s)):
            ss = s[i:i+len(p)]
            # skip cases
            if len(ss) != len(p):
                continue
            hist_ss = get_hist(ss)
            hist_p  = get_hist(p)
            if hist_ss == hist_p:
                res.add(i)
        return list(res)


'''
try - 2 that barely works
def xprint(*args, **kwargs):
    return
    print("".join(map(str,args)), **kwargs)

import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        s_lookup = collections.Counter()
        p_lookup = collections.Counter(p)
        xprint(f"pl:{p_lookup}")

        ns = len(s)
        np = len(p)
        if np>ns: return res
        xprint(f"searching for {p} in {s}")
        for i in range(ns):
            xprint(f"examining {i}|{s[i-np+1:i+1]}")
            s_lookup[s[i]]+=1
            if i >= np:
                # delete count of prev letter
                if s_lookup[s[i-np]] == 1:
                    xprint(f"del key {s[i-np]}")
                    del s_lookup[s[i-np]]
                else:
                    s_lookup[s[i-np]]-=1
            # xprint(f"i:{i}|{s[i:i+np]}")
            xprint(f"sl:{s_lookup}")
            if s_lookup == p_lookup:
                match_index = i - np + 1
                xprint(f"<*> matched at {match_index}: {s[match_index:i+1]}>>")
                res.append(match_index)
            else:
                xprint("no match")
        return list(res)
'''

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[s[i]] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output
      
'''
another soln
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output

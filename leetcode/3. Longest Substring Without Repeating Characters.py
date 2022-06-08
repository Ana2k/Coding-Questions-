#with while loop counter
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,k = 0,0,1
        n = len(s)
        if n==1 or n==0:
            return n
        #sliding window approach using hash maps
        res = 0
        c = Counter()
        while(r<n):
            c[s[r]]+=1
            while(c[s[r]]!=k and l<r):#would have been k here instead of 1 for k distinct characters
                if c[s[l]]-1>=0:
                    c[s[l]]-=1
                l+=1
            res = max(r-l+1,res)
            r+=1
        return res

#hashmap method without while loop
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        slow = fast = 0
        di_idx = defaultdict(lambda : -1)
        for fast in range(len(s)):
            ch = s[fast]
            if di_idx[ch]!=-1:
                slow = max(slow,di_idx[ch]+1)
            di_idx[ch] = fast
            res = max(res,fast-slow+1)
        return res
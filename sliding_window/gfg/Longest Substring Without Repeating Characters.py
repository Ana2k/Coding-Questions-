#Question Link : https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
#Secret code : This one finds the substring as well :)
from collections import defaultdict
class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        n = len(S)
        if n<=1:
            return n
        stk = res =""
        maxi =  0
        for ch in S:
            if ch in stk:
                #update stk
                idx = stk.index(ch)
                stk = stk[idx+1:]
            stk+=ch
            n = len(stk)
            if maxi<n:
                maxi = max(maxi,n)
                res = stk
        return maxi




from collections import defaultdict
class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        n = len(S)
        if n<=1:
            return n
        #di stores the last occurence of the character's index
        di = defaultdict(lambda : -1)
        old = res = 0
        for i in range(n):
            ch = S[i]
            if di[ch]!=-1:
                #old character index updated.
                old = max(old,di[ch]+1)
            di[ch] = i
            res = max(res,i-old+1)
        return res
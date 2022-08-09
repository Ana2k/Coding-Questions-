class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #dp stores the inner elements and thier count
        dp = defaultdict(lambda : 0)
        res = 1
        for word in sorted(words,key = len):
            dp[word] = 1
            for i in range(len(word)):
                inner = word[:i]+word[i+1:]
                if dp[inner]!=0:
                    dp[word] = max(dp[word],dp[inner]+1)
                    res = max(res,dp[word])
        return res
        #instead of res, we can also use, 
        #max(dp.values())
        #this is in this aspect like LIS
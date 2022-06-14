#daily challenge June 14'22
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # subtract double the lcs from total length
        # lcs link : https://leetcode.com/problems/longest-common-subsequence/
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        lcs = dp[m][n]
        return (m+n)-2*lcs
        
            
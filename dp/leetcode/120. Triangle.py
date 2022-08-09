class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                if j+1<n:
                    triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
                else:
                    triangle[i][j]+=(triangle[i+1][j])
        return triangle[0][0]
        #could use a seperate dp = [[0]*(n+1) for i in range(n+1)] as well
        # and then for i in range(n-1,-1,-1) and for j in range(i+1)
        # and dp[i][j] = triangle[i][j]+min(dp[i+1][j],dp[i+1][j+1])
        # return dp[0][0]
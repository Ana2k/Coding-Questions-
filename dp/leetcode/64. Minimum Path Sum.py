class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #how to even think about this?
        # or these kinds of questions?
        #bfs
        # https://leetcode.com/problems/minimum-path-sum/discuss/793480/python-DP-with-explanation
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*(n) for row in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0:
                    #firs row can only take left values
                    #unless they are first elements
                    if j==0:
                        dp[i][j] = grid[i][j]
                    else:
                        #LEFT
                        dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j==0:
                    #we have dealt with the case of first element.
                    if i==0:
                        dp[i][j] = grid[i][j]
                    else:
                        #UP
                        dp[i][j] = dp[i-1][j]+grid[i][j]
                else:    
                    #KEY STATEMENTS                    
                    up = dp[i-1][j]
                    left = dp[i][j-1]
                    dp[i][j] = min(up,left)+grid[i][j]
                # print(dp)
        return dp[-1][-1]
                
            

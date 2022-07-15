def knapSack(self,W, wt, val, n):
        dp = [[-1 for col in range(W+1)] for row in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                #base condition
                if i==0 or j==0:
                    dp[i][j]=0
                #recursive calls
                elif wt[i-1]<=W:
                    #(n,W)Memo---(i,j)BottomUp
                    #knap(W,n-1)---not take --- dp[i-1][j]
                    #knap(W-wt[n-1],n-1)---take --- dp[i-1][j-wt[i-1]]
                    dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][W]
                

        #base condition
        # if n==0 or W==0:
        #     return 0
        #choice diagram
        # if wt[n-1]<=W:
        #     choose or dont choose max of that


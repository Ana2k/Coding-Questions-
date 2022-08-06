#look at the paramas, to create size of the memo table
#wee basically only need to add two lines..

def knapSack(self,W, wt, val, n):
        dp = [[-1 for col in range(W+1)] for row in range(n+1)]
        def knap(W, wt, val, n):
            #base condition
            if(n==0 or W==0):
               return 0
               
            #added this dp table
            if dp[n][W]!=-1:
                return dp[n][W]
            
            #CHOICE DIAGRAM
            if (wt[n-1]<=W):
                #you can either take or not take the values
                dp[n][W] = max(val[n-1]+knap(W-wt[n-1],wt,val,n-1),knap(W,wt,val,n-1))
                return dp[n][W]
            else:
                dp[n][W] = knap(W,wt,val,n-1)
                return dp[n][W]
        maxProfit = knap(W,wt,val,n)
        # print(dp)
        return maxProfit

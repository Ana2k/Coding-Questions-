class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        #recursion--> to memoisations
        dp = [[0 for i in range(sum+1)] for j in range(N+1)]
        
        #base conditions
        #think of the smallest possible values
        #if sum==0 and if n==0
        
        #if N==0 then nothing can make this value
        for j in range(sum+1):
            dp[0][j] = 0
        #if sum==0>> anything will make this, >>fil dp with True or 1
        for i in range(N+1):
            dp[i][0] = 1
            
        for i in range(1,N+1):
            for j in range(1,sum+1):
                #choice diagram
                #you either choose a number of dont
                if arr[i-1]<=j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][sum]
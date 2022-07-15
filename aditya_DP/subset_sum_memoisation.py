#User function Template for python3
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        #recursion--> to memoisations
        dp = [[-1 for i in range(sum+1)] for j in range(N+1)]
        
        def memo(N,arr,sum):
            #Base conditions
            #everything will make this
            if sum==0:
                dp[N][sum]=1
                return dp[N][sum]
            #nothing can ever make this
            #the sequence of these two matter a lot
            #bcs we need the zeroth element to be 0, as no numbers--> sum up to nothing not 0
            
            if (N==0):
                dp[N][sum]=0
                return dp[N][sum]
            
            if dp[N][sum]!=-1:
                return dp[N][sum]
            #choice diagrams
            #either we choose a value or we dont to check for subset sums
            if arr[N-1]<=sum:
                take = memo(N-1,arr,sum-arr[N-1])
                not_take = memo(N-1,arr,sum)
                dp[N][sum] = take or not_take
                return dp[N][sum]
            else:
                dp[N][sum] = memo(N-1,arr,sum)
                return dp[N][sum]
        return memo(N,arr,sum)

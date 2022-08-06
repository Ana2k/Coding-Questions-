#for memoisation approach please check this link
# https://github.com/cl2333/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions/blob/c9be833fe96f0333ab537e378b3989e47c659d54/15.%20Pattern%20%2001%20Knapsack%20(Dynamic%20Programming)/Problem%20Challenge%201%20-%20Count%20of%20Subset%20Sum%20(hard)%20.py#L84
class Solution:
	def perfectSum(self, arr, n, sum):
		#the code for this is similar to isSubseetSum problem only difference is the add symbol 
		#instead of the or symbol
		# code here 
        #recursion--> to memoisations
        dp = [[0 for i in range(sum+1)] for j in range(n+1)]
        mod=1000000007
        #base conditions
        #think of the smallest possible values
        #if sum==0 and if n==0
        
        #if N==0 then nothing can make this value
        for j in range(sum+1):
            dp[0][j] = 0
        #if sum==0>> anything will make this, >>fil dp with True or 1
        for i in range(n+1):
            dp[i][0] = 1
            
        for i in range(1,n+1):
            for j in range(sum+1):
                #choice diagram
                #you either choose a number of dont
                if arr[i-1]<=j:
                    dp[i][j] = (dp[i-1][j-arr[i-1]]+dp[i-1][j])%mod
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][sum]
		
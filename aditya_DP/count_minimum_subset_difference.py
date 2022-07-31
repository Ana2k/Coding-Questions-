#aim would be to make sum1-sum2 = 0 or tend to 0
		#that is the minimum when you think in terms of mod.
		#the next thing is, how will you find the minimum? think the max that 
		#both the sums can be is sum//2 right?
		#so, think what do you actually need?
		#you need to know if there are any subsets for this particular value you chose as sum right?
		#you need to do so for, all the numbers from 0 to sum//2 and check res  = total-that_number,
		#and update this res.
		#now how to obtain the values that will give the valid sums??
		#we, use the equal partitionsums.
		#think dp truth table-->equal partition. use the last row, we only need that row.
		#to find the possible to reach, values,till sum//2 as subsets.
		#(baaki toh total-that number exists already.)
def minDifferenceTabulation(self, arr, n):
		# code here
		total = sum(arr)
		n = len(arr)
		dp = [[0]*(total+1) for i in range(n+1)]
		#base cases for equal partition where what?
		#n==0, no numbers to select from => that means no subsets, unless sum==0, then true
		#sumi=0
		for i in range(n+1):
		    dp[i][0] = 1
		    
        for j in range(1,total+1):
		    dp[0][j] = 0
# 		print(dp)
		for i in range(1,N+1):
		    for j in range(1,total+1):
		        if arr[i-1]<=j:
		            dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
		        else:
		            dp[i][j] = dp[i-1][j]
# 		print(dp)
		#equal partition wala,
		
# 		print(dp)
		#now find the last row, mei last True value, such that 
		#that value was lesser than equal to sum//2
        res = float("inf")
		for j in range(total//2+1):
		    if dp[n][j]==1:
		        res = min(res,total-2*j)
		     
        return res
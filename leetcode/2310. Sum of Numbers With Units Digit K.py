#UNDERSTANDING AND DIFFERENCE BETWEEN BOUNDED AND UNBOUNDED KNAPSACK
#AND USING IT OVER COIN CHANGE PROBLEM.
#dp - dynamic programming - coin change derivative
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num==0:
            return 0
        if k%2==0 and num%2==1:
            return -1
        if num==k:
            return 1
        coins = [x for x in range(num+1) if x%10==k]
        
        # https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
        #we can also do
        #copy = k
        #while(k<=3000 and k<=num):
        #   arr.append(k); k+=10
        #k = copy
        
        #ditto code from gfg
        dp = [float("inf") for i in range(num+1)]
        #0 can be made in 0 number of ways.
        dp[0] = 0

        
        for i in range(1,num+1):
            #go through all the coins smaller than i
            for j in range(len(coins)):
                if coins[j]<=i:
                    sub_res = dp[i-coins[j]]
                    if sub_res!=float("inf") and sub_res+1<dp[i]:
                        dp[i] = sub_res+1
                            
        if dp[num]==float("inf"):
            return -1
        return dp[num]
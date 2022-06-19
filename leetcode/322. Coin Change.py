class Solution:
    def coinChange(self, coins: List[int], num: int) -> int:
        #reference https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
        n = len(coins)
        dp = [float("inf") for i in range(num+1)]
        dp[0]=0
        for i in range(1,num+1):
            #check for all the coins smaller than the given amount
            for j in range(len(coins)):
                if coins[j]<=i:
                    #same concept as two pointer di[target-i]
                    sub_res = dp[i-coins[j]]
                    if sub_res!=float("inf") and sub_res+1<dp[i]:
                        dp[i] = 1+sub_res
        if dp[num]==float("inf"):
            return -1
        return dp[num]
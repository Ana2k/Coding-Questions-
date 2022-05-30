#BOTTOM UP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]*(n+1)
        
        dp[1]=1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
            
            print(dp[i])
            
        return dp[n]
        
#RECURSIVE TO MEMOISATIONS -TOP DOWN
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i<=2:
                return i
            if i not in memo:
                memo[i] = dp(i-1)+dp(i-2)
            return memo[i]
        memo = {}
        # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
        # store the result inside a hashmap to refer to in the future.
        return dp(n)
    
    #NON MEMOIZED TOP DOWN
            
        
        
        
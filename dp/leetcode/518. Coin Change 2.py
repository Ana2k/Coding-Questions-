# Method 3 : the bottom up part of https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
#Method 2:
class Solution:
    def change(self, amounts: int, coins: List[int]) -> int:
        #Method 2
        # great explanations : https://leetcode.com/problems/coin-change-2/discuss/1600337/Java-%2B-DP-%2B-Detailed-Explanation
        n = len(coins)
        dp = [0 for i in range(amounts+1)]
        dp[0] = 1
        # print(dp)

        for i in range(len(coins)):
            for j in range(coins[i],amounts+1):
                dp[j]+=dp[j-coins[i]]
        # print(dp)
        return dp[amounts]

#Method 1
class Solution:
    def change(self, amounts: int, coins: List[int]) -> int:
        #youtube playlist : https://www.youtube.com/watch?v=I4UR2T6Ro3w&t=510s&ab_channel=AdityaVerma >> explanation
        #related question : https://leetcode.com/contest/weekly-contest-298/problems/sum-of-numbers-with-units-digit-k/
        # https://leetcode.com/problems/coin-change-2/discuss/675186/Python3-DP-Solution-O(mn)-Time-and-Space >> code
        #The 2d array method.
        n = len(coins)
        dp = [[0]*(amounts+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,amounts+1):
                if coins[i-1]<=j:
                    dp[i][j] = (dp[i-1][j]+dp[i][j-coins[i-1]])
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[n][amounts]
        
        
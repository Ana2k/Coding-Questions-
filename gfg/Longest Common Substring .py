
#Method 2 : the sliding window one
class Solution:
    def longestCommonSubstr(self, A, B, n, m):
        # code here
        #sliding window for this is also feasible
        maxi = 0
        start = 0
        for end in range(n):
            if A[start:end+1] in B:
                maxi = max(maxi,end-start+1)
            else:
                while(A[start:end+1] not in B):
                    #we cant use a subA here, as start is 
                    #constantly changing in value.
                    start+=1
        return maxi
#Method 1 : The usual...i am a bit confused but works kind
#i am personally thinking, what makes this question different from
# @longest common subsequence?
#why the difference in else statement?
#is it bcs its behaving like a substring?
class Solution:
    def longestCommonSubstr(self, A, B, m, n):
        # code here
        #bottom_up
        m = len(A)
        n = len(B)
        
        dp = [[0]*(n+1)for i in range(m+1)]
        maxi = 0
        #rows
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1]==B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    maxi = max(maxi,dp[i][j])
                else:
                   dp[i][j]=0
        # print(dp)
        return maxi

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# The first method is sliding window with a single for nested while loop,
# And lesser number of lines(less number of lines with less processing means a faster code in python). The sliding window approach is closer to O(n) complexity than the O(n^2) complexity for each single test case.

# The second method uses two seperate for nested for loops and almost in all cases runs till the end, meaning almost all test cases run a O(n^2)
# Remember the bigO are the worst case complexity.
# So for both even if big O is same, the average run time complexity is better for the first one.
# I hope you could understand my explanation :)
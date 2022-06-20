class Solution:
    def countBits(self, n: int) -> List[int]:
        #liked this discussion thread.
        #https://leetcode.com/problems/counting-bits/discuss/1818314/C%2B%2B-oror-Single-Pass-O(N)-TC-O(N)-SC-oror-Easy-To-Understand
        
        
        dp = [0]*(n+1)
        for i in range(1,n+1):
            if(i&1): #if i is odd
                dp[i] = dp[i-1]+1
                #add one to the even format
            else:
                dp[i] = dp[i//2]
        return dp
            
                
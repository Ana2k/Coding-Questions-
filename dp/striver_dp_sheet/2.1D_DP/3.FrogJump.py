#VIDEO LINK : https://www.youtube.com/watch?v=EgG3jsGoPvQ&ab_channel=takeUforward
#EXPLANATION LINK : https://takeuforward.org/data-structure/dynamic-programming-frog-jump-dp-3/
#QUESTION LINK : https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos
def solve():
    n = int(input())
    heights = list(map(int,input().split()))
    dp = [-1 for _ in range(n)]
    #iterative
    #base case
    dp[0] = 0
    for i in range(1,n):
        jumpOne = dp[i-1]+abs(heights[i]-heights[i-1])
        if i>=2:
            jumpTwo = dp[i-2]+abs(heights[i]-heights[i-2])
        dp[i] = min(jumpOne,jumpTwo)
    
    #recursion+DP
    def fRD(n,heights):
        #is the minimal cost to reach index n
        if n==0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        jumpOne = fRD(n-1,heights)+abs(heights[n]-heights[n-1])
        jumpTwo = float("inf")
        if n>=2:
            jumpTwo = fRD(n-2,heights)+abs(heights[n]-heights[n-2])
        dp[n] = min(jumpOne,jumpTwo)
        return dp[n]
    # print((f(n-1,heights)))

t = int(input())
for _ in range(t):
    solve()   

# VIDEO LINK :https://www.youtube.com/watch?v=Kmh3rhyEtB8&ab_channel=takeUforward
# EXPLANATION LINK : https://takeuforward.org/data-structure/dynamic-programming-frog-jump-with-k-distances-dp-4/
# QUESTION LINK : https://atcoder.jp/contests/dp/tasks/dp_b
import sys
#Recursion
def f(n,dp):
    if dp[n]!=-1:
        return dp[n]
    #base case
    if n==0:
        return 0
    minSteps = float("inf")
    for step in range(1,k+1):
        if n-step>=0:#to balance the index of heights.
            jumps = f(n-step)+abs(heights[n]-heights[n-step])
            minSteps = min(minSteps,jumps)
    dp[n] = minSteps
    return dp[n]
    
def solve():
    # input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    input = sys.stdin.readline
    n,k = map(int,input().split())
    heights = list(map(int,input().split()))
    dp = [-1]*(n)
    dp[0] = 0
    for i in range(1,n):
        minStep = float("inf")
        for step in range(1,k+1):
            if i-j>=0:
                jump = dp[i-step]+abs(heights[i]-heights[i-step])
                minStep = min(minStep,jump)
        # print(dp," ",minStep)
        dp[i] = minStep
    sys.stdout.write(str(dp[n-1]))
    # print(fRD(n-1))
    # print(dp)

t = 1
for _ in range(t):
    solve()    
#first think of the recursion then 
#add the dp steps.
def rec(level,n,m,dp):
    #base case
    if(level>n):
        return 0
    if level==n:
        return 1
    
    #cache
    if dp[level]!=-1:
        #means this was computed
        return dp[level]
    #choice
    #compute
    ans = 0
    for step in range(1,m+1):
        #check
        if(level+step<=n):
        	ans+=rec(level+step,n,m,dp)
    dp[level] = ans
    return ans
    
def solve():
    n,m = map(int,input().split())
    #cache --> the number of ways to reach the ith stair
    dp = [-1]*(n)
    ans = rec(0,n,m,dp)
    # print(dp)
    print(ans)
    #level
    #level-- the ith step i am on
    #choice
    #check
    #move
    
t = int(input())
while(t):
    solve()
    t-=1
    
    
    

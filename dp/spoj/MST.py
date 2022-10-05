# https://www.spoj.com/problems/MST1/
t = int(input())
#PURE RECURSION
MAXI = 2*(10**7)+1
dp = [0]*(MAXI+1)
# def rec(n):
#     if n==1:
#         return 0
#     if dp[n]:
#         return dp[n]
#     if n%2==0 and n%3:
#         step = 1+min(rec(n//2),rec(n-1))
#     elif n%3==0 and n%2:
#         step = 1+min(rec(n//3),rec(n-1))
#     elif n%3==0 and n%2==0:
#         step = 1+min(rec(n//2),rec(n//3),rec(n-1))
#     else:
#         step = 1+rec(n-1)
#     dp[n] = step
#     return dp[n]

for _ in range(t):
    n = int(input())
    # ans = rec(n)
    for i in range(2,n+1):
        if i%2==0 and i%3:
            dp[i] = 1+min(dp[i-1],dp[i//2])
        elif i%3==0 and i%2:
            dp[i] = 1+min(dp[i-1],dp[i//3])
        elif i%2==0 and i%3==0:
            dp[i] = 1+min(dp[i-1],dp[i//2],dp[i//3])
        else:
            dp[i] = 1+(dp[i-1])
    # return dp[n]
    ans = dp[n]
    print("Case %d: %d"%(_+1,ans))
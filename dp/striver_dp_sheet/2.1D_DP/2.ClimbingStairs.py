def countDistinctWays(nStairs: int) -> int:
        #fibonacci.
#     n = int(input("Enter fib number"))
    n = nStairs
    dp =[-1]*(n+1)
    #memoisation
    MOD=1000000007
    def f(n):
        if n<=1:
            dp[n] = 1    
        #RECURSIVE
        # return f(n-1)+f(n-2)
        if dp[n]!=-1:return dp[n]%(MOD)
        dp[n]= f(n-1)+f(n-2)
#         print(dp)
        return dp[n]%(MOD)
    return f(n)%(MOD)
#easy for tabulation and o(1) as well.
#check this link : https://takeuforward.org/data-structure/dynamic-programming-climbing-stairs/


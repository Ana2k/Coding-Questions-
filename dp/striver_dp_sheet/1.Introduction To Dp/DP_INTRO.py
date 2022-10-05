#fibonacci.
n = int(input("Enter fib number"))
dp =[-1]*(n+1)

#memoisation
def f(n):
    if n<=1:
        dp[n] = n
    else:#RECURSIVE
        # return f(n-1)+f(n-2)
        if dp[n]!=-1:return dp[n]
        dp[n]= f(n-1)+f(n-2)
        # print(dp)
    return dp[n]
# print(f(n))
#easy for tabulation and o(1) as well.
#check this link for the same : https://takeuforward.org/data-structure/dynamic-programming-introduction/



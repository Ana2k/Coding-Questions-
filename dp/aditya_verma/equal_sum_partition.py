#6.2
class Solution:
    def equalPartition(self, N, arr):
        #recursion
        sumi = sum(arr)
        if sumi%2!=0:
            return False
        memo = [[-1 for i in range(sumi+1)]for j in range(N+1)]
        def isSubsetSumMemo(arr,N,sumi):
            #ditto as the previous question
            
            if N==0 and sumi!=0:
                memo[N][sumi]=0
                return memo[N][sumi]
            if sumi==0:
                memo[N][sumi] = 1
                return memo[N][sumi]
            if memo[N][sumi]!=-1:
                return memo[N][sumi]
            if arr[N-1]<=sumi:
                #you can take or not take this
                take = isSubsetSum(arr,N-1,sumi-arr[N-1])
                not_take = isSubsetSum(arr,N-1,sumi)
                memo[N][sumi] = take or not_take
                return memo[N][sumi]
            else:
                not_take = isSubsetSum(arr,N-1,sumi)
                memo[N][sumi] = not_take
                return memo[N][sumi]
        def isSubsetSumTable(arr,N,sumi):
            for j in range(sumi+1):
                memo[0][j] = 0
            for i in range(N+1):
                memo[i][0] = 1
            for i in range(N+1):
                for j in range(sumi+1):
                    if arr[i-1]<=j:
                        memo[i][j] = memo[i-1][j] or memo[i-1][j-arr[i-1]]
                    else:
                        memo[i][j] = memo[i-1][j]

        return isSubsetSumTable(arr,N,sumi//2)        
        # return isSubsetSumMemo(arr,N,sumi//2)

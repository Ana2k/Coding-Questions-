from collections import defaultdict
class Solution:
    
    
    def findPath(self, m, n):
        res = []
        visited = defaultdict(lambda : False)
        def dfs(m, n, visited, res, path, i, j):
            if i<0 or i>=n or j<0 or j>=n or m[i][j]==0 or visited[(i,j)]==True:
                return
            
            if i==n-1 and j==n-1:
                res.append(path)
                return
            
            visited[(i,j)] = True
            dfs(m,n,visited,res,path+'D',i+1,j)
            dfs(m,n,visited,res,path+'U',i-1,j)
            dfs(m,n,visited,res,path+'R',i,j+1)
            dfs(m,n,visited,res,path+'L',i,j-1)
            visited[(i,j)] = False
    
        dfs(m,n,visited,res,"",0,0)
        
        return res
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        res = ob.findPath(matrix, n[0])
        res.sort()
        if len(res) == 0 :
            print(-1)
        else:
            for x in res:
                print(x,end = " ")
            print()
# } Driver Code Ends
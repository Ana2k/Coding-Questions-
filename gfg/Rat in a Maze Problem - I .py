from collections import defaultdict
class Solution:
    def findPath(self, m, n):
        res = []
        visited = defaultdict(lambda : False)
        def dfs(path, i, j):
            nonlocal m,n,visited,res
            if i<0 or i>=n or j<0 or j>=n or m[i][j]==0 or visited[(i,j)]==True:
                return
            
            if i==n-1 and j==n-1:
                res.append(path)
                return
            
            visited[(i,j)] = True
            dfs(path+'D',i+1,j)
            dfs(path+'U',i-1,j)
            dfs(path+'R',i,j+1)
            dfs(path+'L',i,j-1)
            visited[(i,j)] = False
    
        dfs("",0,0)
        
        return res
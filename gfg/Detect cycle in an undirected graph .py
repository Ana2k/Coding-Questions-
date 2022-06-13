#User function Template for python3
#june 11 - graph
from collections import defaultdict
class Solution:
    def dfs(self,currnode,parent,adj,visited,dfsVis):
        visited[currnode] = True
        for node in adj[currnode]:
            if visited[node]==False:
                if self.dfs(node,currnode,adj,visited,dfsVis):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent!=node:
                return True
                
        
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        # https://www.youtube.com/watch?v=uzVUw90ZFIg - striver explanation
        visited = defaultdict(lambda : False)
        for i in range(V):
            if(visited[i]==False):
                cycle = self.dfs(i,-1,adj,visited)
                if cycle:
                    return True
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends
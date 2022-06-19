#june 11 - graph - cycle in undirected
from collections import defaultdict
class Solution:
    def dfs(self,currnode,parent,adj,visited,dfsVis):
        visited[currnode] = True
        for node in adj[currnode]:
            if visited[node]==False:
                cycle = self.dfs(node,currnode,adj,visited,dfsVis)
                if cycle:
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
#graph  - cycle in a directed graph
#backtracking over dfsVis
from collections import defaultdict
class Solution:
    def dfs(self,currnode,adj,vis,dfsVis):
        vis[currnode] = True
        dfsVis[currnode] = True
        for node in adj[currnode]:
            if vis[node]==False:
                cycle = self.dfs(node,adj,vis,dfsVis)
                if cycle:
                    return True
            elif dfsVis[node]==True:
                return True
        #this cycle ended now clear the dfsVis currnode for other cycles.
        dfsVis[currnode] = False
        return False
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        # https://www.youtube.com/watch?v=uzVUw90ZFIg - striver explanation
        #visited is keeping track of overall visits of node
        #but dfsvisited is keeping track if the node was visited in the current movement.
        vis = defaultdict(lambda : False)
        dfsVis = defaultdict(lambda : False)
        for i in range(V):
            if vis[i]==False:
                cycle = self.dfs(i,adj,vis,dfsVis)
                if cycle:
                    return True
        return False

#graph - dfs
from collections import defaultdict
class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        res = []
        vis = defaultdict(lambda : False)
        def dfs(currnode):
            nonlocal res,vis
            vis[currnode] = True
            res.append(currnode)
            for node in adj[currnode]:
                if vis[node]==False:
                    vis[node] = True
                    dfs(node)
        dfs(0)
        return res
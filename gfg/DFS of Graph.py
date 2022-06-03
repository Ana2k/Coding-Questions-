#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        res = []
        visited = defaultdict(lambda : False)
        def dfs(node):
            nonlocal res,visited
            res.append(node)
            visited[node] = True
            for v in adj[node]:
                if visited[v]==False:
                    visited[v] = True
                    dfs(v)
        dfs(0)
        return res
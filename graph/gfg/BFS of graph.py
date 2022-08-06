#graph - bfs
from collections import deque,defaultdict
class Solution:
    # https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        res = []
        vis = defaultdict(lambda : False)
        q = deque([0])
        while(q):
            currnode = q.popleft()
            res.append(currnode)
            for node in adj[currnode]:
                if vis[node]==False:
                    vis[node] = True
                    q.append(node)
        return res
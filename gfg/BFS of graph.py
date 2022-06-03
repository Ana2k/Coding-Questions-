from collections import deque,defaultdict
class Solution:
    # https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        res = []
        q = deque([0])
        visited = defaultdict(lambda : False)
        while(q):
            top = q.popleft()
            res.append(top)
            for node in adj[top]:
                if visited[node] == False:
                    visited[node] = True
                    q.append(node)
        return res
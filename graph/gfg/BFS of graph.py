#graph - bfs
from collections import deque,defaultdict
class Solution:
    # https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    #Function to return Breadth First Traversal of given graph.
    #a cool explanation is also : https://takeuforward.org/graph/breadth-first-search-bfs-level-order-traversal/

    def bfsOfGraph(self, V, adj):
        res = []
        q = deque([0])
        vis = defaultdict(lambda : False)
        while(q):
            currnode = q.popleft()
            res.append(currnode)
            for node in adj[currnode]:
                if vis[node]==False:
                    vis[node] = True
                    q.append(node)
        return res
        # res = []
        # vis = defaultdict(lambda : False)
        # q = deque([0])
        # while(q):
        #     currnode = q.popleft()
        #     res.append(currnode)
        #     for node in adj[currnode]:
        #         if vis[node]==False:
        #             vis[node] = True
        #             q.append(node)
        # return res
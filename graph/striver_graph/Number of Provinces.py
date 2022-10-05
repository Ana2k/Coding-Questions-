#Question Link :
#  https://practice.geeksforgeeks.org/problems/number-of-provinces/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-provinces

# from collections import deque
class Solution:
    def numProvinces(self, adj, V):
        #with DFS
        #check number of Islands question for better reference
        vis = [False for _ in range(V)]
        #can use vis =  defaultdict(lambda : False)
        def dfs(currnode):
            vis[currnode] = True
            for edge in range(V):
                if adj[currnode][edge] and vis[edge]==False:
                    dfs(edge)
        def bfs(currnode):
            q = deque([currnode])
            vis[currnode] = True
            while(q):
                node = q.popleft()
                for edge in range(V):
                    if adj[currnode][edge] and vis[edge]==False:
                        vis[edge]= True
                        q.append(edge)
        #QUESTION ESSENCE = COUNT THE NUMBER OF DFS OR BFS CALLS YOU HAVE TO MAKE
        #To traverse the entire graph.
        num = 0
        for i in range(V):
            if vis[i]==False:
                num+=1
                dfs(i)
        return num
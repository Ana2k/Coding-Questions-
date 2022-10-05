#QUestion link : https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #isConnected is the adjoincy matrix
        #HERE from -->  https://practice.geeksforgeeks.org/problems/number-of-provinces/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-provinces
        #Striver graph begginers questions
        # you can also recreate the isConnected to create a adjacent list
        # implementation in  : https://leetcode.com/problems/number-of-provinces/discuss/2655239/Python-Simple-recursion-dfs-98-faster
        #number of Vertexes
        V = len(isConnected)
        vis = set()
        def dfs_no_extra_adj(currnode):
            #just used isConnected for this one.
            vis.add(currnode)
            for edge in range(V):
                if isConnected[currnode][edge]==1 and edge not in vis:
                    dfs(edge)

        def dfs(currnode):
            vis.add(currnode)
            for node in adj[currnode]:
                if node not in vis:
                    dfs(node)

        #create an adj
        adj = defaultdict(set)
        for i in range(V):
            for j in range(V):
                if isConnected[i][j]:
                    if i!=j:
                        adj[i].add(j)
                        adj[j].add(i)
        #bfs
        def bfs(currnode):
            q = deque([currnode])
            vis.add(currnode)
            while(q):
                node = q.popleft()
                for edge in adj[node]:
                    if edge not in vis:
                        vis.add(edge)
                        q.append(edge)
        num = 0
        #check the number of calls to the dfs
        for i in range(V):
            if i not in vis:
                num+=1
                dfs(i)
        return num
                
            
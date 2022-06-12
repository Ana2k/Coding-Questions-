from collections import defaultdict
class Solution:
    
		#dfs first
	def dfs(self,currnode,parent,adj,visited):
		    visited[currnode] = True
		    for node in adj[currnode]:
		        if visited[node]==False:
		            #do dfs
		            if self.dfs(node,currnode,adj,visited):
		                return True
    		    # If an adjacent vertex is
                # visited and not parent
                # of current vertex,
                # then there is a cycle
                elif parent!=node:
                    return True
	def isCycle(self, V, adj):
	    #V is a number of vertices.
		#Code here
# 		also striver https://www.youtube.com/watch?v=Y9NFqI6Pzd4&t=1141s&ab_channel=takeUforward
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
		visited = defaultdict(lambda : False)
		#Function to detect cycle in an undirected graph.

		for i in range(V):
		    #wee check if the node is untraveresed.
		    if(visited[i]==False):
		        cycle = self.dfs(i,-1,adj,visited)
		        if cycle==True:
		            return True
        return False
		        
		    
		

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
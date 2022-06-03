#dfs
class Solution:
    from collections import defaultdict
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs
        # https://leetcode.com/problems/number-of-islands/discuss/1919711/Standard-Template-Using-BFS-in-Python-Foundation-of-All-Similar-Questions!
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        #use visited? yes!
        self.visited = defaultdict(lambda : False)
        totalRow = len(grid)
        totalCol = len(grid[0])
        island = 0
        def dfs(row,col):
            if row<0 or col<0 or row>=totalRow or col>=totalCol or grid[row][col]!="1": return None
            grid[row][col] = "0"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)
            dfs(row,col+1)
            
        for row in range(totalRow):
            for col in range(totalCol):
                if(grid[row][col]=="1"):
                    dfs(row,col)
                    island+=1
        return island
#bfs
class Solution:
    from collections import defaultdict
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs
        # https://leetcode.com/problems/number-of-islands/discuss/1919711/Standard-Template-Using-BFS-in-Python-Foundation-of-All-Similar-Questions!
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        #use visited? yes!
        self.visited = defaultdict(lambda : False)
        totalRow = len(grid)
        totalCol = len(grid[0])
        island = 0
        def bfs(row,col):
            q = deque()
            q.append((row,col))
            grid[row][col] = 0
            while(q):
                x,y = q.popleft()
                for dx,dy in dirs:
                    r = x+dx
                    c = y+dy
                    if 0<=r<totalRow and 0<=c<totalCol and grid[r][c]=="1": 
                        grid[r][c] = "0"
                        q.append((r,c))
                    
        for row in range(totalRow):
            for col in range(totalCol):
                if(grid[row][col]=="1"):
                    bfs(row,col)
                    island+=1
        return island
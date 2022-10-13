#Question link 
# Leetcode : https://leetcode.com/problems/rotting-oranges/submissions/
#GFG : 
#Can only be done better with bfs
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #check visual studio for the walls and gates problem this is a similar question.
        # this link also helped
        # https://leetcode.com/problems/rotting-oranges/discuss/1437571/Python-Clean-and-concise-BFS-solution
        fresh,empty,rotten = 1,0,2
        
        rows_n = len(grid)
        if rows_n==0:
            return -1
        cols_n = len(grid[0])
        
        q = deque()
        count_fresh = 0
        for i in range(rows_n):
            for j in range(cols_n):
                if grid[i][j] == fresh:
                    count_fresh+=1
                elif grid[i][j] == rotten:
                    q.append((i,j))
        
        #all the four dirs
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        #bfs
        time = 0
        while q and count_fresh:
            time+=1
            for _ in range(len(q)):
                row,col = q.popleft()
                #visit neighbours
                for dr,dc in dirs:
                    r = row+dr
                    c = col+dc
                    if 0<=r<rows_n and 0<=c<cols_n and grid[r][c]==fresh:
                        #change the fresh into rotten. :)
                        grid[r][c] = rotten
                        q.append((r,c))
                        count_fresh-=1
            
        return time if count_fresh==0 else -1
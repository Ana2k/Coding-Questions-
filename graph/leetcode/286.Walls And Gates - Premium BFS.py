# https://www.youtube.com/watch?v=DvzbzYY2Ank&ab_channel=CodingBlocks
# https://www.lintcode.com/problem/663/solution/59490
# used both to understand 
#could not run this
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    #question like this = https://leetcode.com/problems/rotting-oranges/
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        walls = -1
        gate = 0
        empty = 2147483647
        if not rooms or not rooms[0]:
            return 
        rows_n = len(rooms)
        cols_n = len(rooms[0])

        q = collections.deque()

        for row in range(rows_n):
            for col in range(cols_n):
                if rooms[row][col] == gate:
                    q.append((row, col))
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        while q:
            #bfs
            row,col = q.popleft()
            for dx,dy in dirs:
                r = row+dx
                c = col+dy
                if(0<=r<rows_n and 0<=c<cols_n and rooms[r][c]==empty):
                    rooms[r][c] = rooms[row][col]+1
                    q.append((r,c))
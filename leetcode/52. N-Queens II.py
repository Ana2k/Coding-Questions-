class Solution:
    def totalNQueens(self, n: int) -> int:
        boards = [[0]*n for i in range(n)]
        self.total_count  = 0
        def isSafe(boards,row,col):
            #     [\
            #       \
            #     ---\Q(row,col)
            #        /
            #       / ]
            # how we are checking each side
            #checking the left side
            for j in range(col):
                if boards[row][j]==1:
                    return False
            #checking upper diagonal
            for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
                if boards[i][j]==1:
                    return False
            #checking lower diagonal
            for i,j in zip(range(row,n),range(col,-1,-1)):
                if boards[i][j]==1:
                    return False
            return True
                
            
        def NQ(boards,col):
            if col==n:
                self.total_count+=1
                return True
            #backtracking here for the board
            for row in range(n):
                if isSafe(boards,row,col):
                    boards[row][col] = 1
                    NQ(boards,col+1)
                    boards[row][col] = 0
            return False
                
            
        NQ(boards,0)
        # print(res)
        return self.total_count
        
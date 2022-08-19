class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #gfg link
        # https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
        # https://leetcode.com/problems/n-queens/discuss/2108334/EAZY-BEGINER-oror-EXPLANATION-FOR-ALL-oror
        board = [[0]*(n) for i in range(n)]
        res = []

        def isSafe(board,row,col):
            for j in range(col):
                if board[row][j]==1:
                    return False
                
            for i,j in zip(range(row,-1,-1),
                           range(col,-1,-1)):
                if board[i][j]==1:
                    
                    return False
            for i,j in zip(range(row,n),
                           range(col,-1,-1)):
                if(board[i][j]==1):
                    return False
            return True

        def NQ(board,col):
            if col==n:
                curr = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if board[i][j]:
                            s+="Q"
                        else:
                            s+="."
                    curr.append(s)
                res.append(curr)
                return True
            for row in range(n):
                if isSafe(board,row,col):
                    board[row][col] = 1
                    NQ(board,col+1)
                    board[row][col] = 0
            return False
                
            
        ans = NQ(board,0)
        return res
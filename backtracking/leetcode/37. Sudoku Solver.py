
#not much ideas about this. 
#so checking up youtube.
#similar Q : 
# https://leetcode.com/problems/valid-sudoku/
# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #think of the subcases
        #what are the rules of suduko? 1) no same numbers in row
        # 2) no same numbers in columns. 3) no same numbers in a grid. 
        # https://www.youtube.com/watch?v=FWAIf_EVUKE&ab_channel=takeUforward
        digi = ["1","2","3","4","5","6","7","8","9"]
        def isValid(board,row,col,ch):
            #check rows and columns
            for i in range(9):
                if board[row][i]==ch:
                    return False
                if board[i][col]==ch:
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3]==ch:
                    return False
            return True
            
        def Solver(board,digi):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col]==".":
                        #check all the characters that are possible
                        for i in range(len(digi)):
                            ch = digi[i]
                            if isValid(board,row,col,ch):
                                board[row][col] = ch
                                if Solver(board,digi):
                                    return True
                                else:
                                    board[row][col] = "."
                        return False
            return True
        Solver(board,digi)
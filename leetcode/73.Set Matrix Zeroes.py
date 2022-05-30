class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #store the indexes of i and j
        idx = []
        row_n = len(matrix)
        col_n = len(matrix[0])
        for i in range(row_n):
            for j in range(col_n):
                if matrix[i][j]==0:
                    idx.append((i,j))
        # now pick up each idx and change all the i and all the j
        for r,c in idx:
            #change all the elements in this row.
            for j in range(0,col_n):
                matrix[r][j] = 0
            #change all the elements in this col.
            for i in range(0,row_n):
                matrix[i][c] = 0        
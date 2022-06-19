#Method 1:
class NumMatrix:
    #no idea how to approach this question or this type of questiosn
    # https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/2104857/PYTHON-oror-EXPLAINED-oror
    def __init__(self, matrix: List[List[int]]):
        #row sum
        self.matrix = matrix
        self.sufMatrix = matrix
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                self.sufMatrix[i][j]+=self.sufMatrix[i][j-1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # loop over and find the row1,col1 and row2,col2
        sumi = 0
        i = row1
        while(i<=row2):
            if col1>0:
                sumi+=self.sufMatrix[i][col2]-self.sufMatrix[i][col1-1]
            else:
                sumi+=self.sufMatrix[i][col2]
            i+=1
        return sumi
#Method 2:
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        # https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/2106422/Python-3-or-Faster-than-94-or-with-comments
        self.dp = [[0 for i in range(col+1)] for j in range(row+1)]
        for i in range(row):
            for j in range(col):
                self.dp[i+1][j+1] = self.dp[i+1][j]+self.dp[i][j+1]+matrix[i][j]-self.dp[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #now we have a prefixsum based array.
        #in that we will add and subtract the terms as correctly as possible
        #now how to find the answer = matrix[i][j] = dp based answer from line 9
        
        return self.dp[row2+1][col2+1]-self.dp[row2+1][col1]-self.dp[row1][col2+1]+self.dp[row1][col1]
        
class Solution_directions:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = c = 0
        n = len(matrix)
        m = len(matrix[0])
        res = []
        #bfs
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def valid(i,j):
            if i<0 or j<0 or i>=n or j>=m or matrix[i][j]=="*":
                return False
            return True
        i=0
        dr,dc = dirs[0]
        currdirs = 0
        while(i<n*m):
            # print((dr,dc)," ",(r,c))
            # print(matrix[r][c])
            res.append(matrix[r][c])
            matrix[r][c] = "*"
            if not valid(r+dr,c+dc):
                currdirs+=1
                dr,dc = dirs[currdirs%4]   
            r=r+dr
            c=c+dc
            i+=1
        return res

class Solution_brute_force:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart = 0
        colStart = 0
        rowEnd = len(matrix)-1
        colEnd = len(matrix[0])-1
        
        if not matrix:
            return []
        
        res = []
        while(rowStart<=rowEnd and colStart<=colEnd):
            for i in range(colStart,colEnd+1):
                res.append(matrix[rowStart][i])
            rowStart+=1
            
            for i in range(rowStart,rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd-=1
            
            if rowStart<=rowEnd:
            
                for i in range(colEnd,colStart-1,-1):
                    res.append(matrix[rowEnd][i])

                rowEnd-=1
            
            if colStart<=colEnd:

                for i in range(rowEnd,rowStart-1,-1):
                    res.append(matrix[i][colStart])

                colStart+=1
        return res
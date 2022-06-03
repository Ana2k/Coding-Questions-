#dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColour: int) -> List[List[int]]:
        # https://leetcode.com/problems/flood-fill/discuss/626514/CPPC%2B%2BEasy-to-understandWell-ExplainedDFS-Flood-Fill
        oldColour = image[sr][sc]
        if oldColour!=newColour: 
            totalRow = len(image)
            totalCol = len(image[0])
            def dfs(i,j,image,newColour):
                #our base cases
                nonlocal totalRow,totalCol
                if(i<0 or j<0 or i==totalRow or j==totalCol or image[i][j]!=oldColour): return
                image[i][j] = newColour
                dfs(i-1,j,image,newColour)
                dfs(i,j-1,image,newColour)
                dfs(i,j+1,image,newColour)
                dfs(i+1,j,image,newColour)
            dfs(sr,sc,image,newColour)
        return image
#bfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColour: int) -> List[List[int]]:
        # https://leetcode.com/problems/flood-fill/discuss/2092266/Iterative-simple-BFS-solution
        oldColour = image[sr][sc]
        if oldColour!=newColour: 
            totalRow = len(image)
            totalCol = len(image[0])
            q = deque()
            q.append([sr,sc])
            while(q):
                # print(q,"1")
                r,c = q.popleft()
                if(totalRow>r>=0 and totalCol>c>=0 and image[r][c]==oldColour):
                    image[r][c] = newColour
                    q.append([r,c+1])
                    q.append([r,c-1])
                    q.append([r+1,c])
                    q.append([r-1,c])
                    # print(q,"2")
        return image
# Question link : 
# Leetcode = https://leetcode.com/problems/flood-fill/
# GFG = https://practice.geeksforgeeks.org/problems/flood-fill-algorithm1856/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=flood-fill-algorithm
class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		oldColour = image[sr][sc]
		if oldColour!=newColor:
		    row_n = len(image)
            col_n = len(image[0])
		    #all the four dirs
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		    def dfs(r,c):
		        nonlocal oldColour,row_n,col_n,newColor
		        #differenc in dfs and bfs majorly is, in dfs we are checking for non validitiy
		        #and in bfs we i mean i usually check for validity.
		        if r<0 or c<0 or r==row_n or c==col_n or image[r][c]!=oldColour:
		            return
		        nonlocal dirs
		        image[r][c] = newColor
		        for dx,dy in dirs:
		            dfs(r+dx,c+dy)
		        
		    dfs(sr,sc)
        return image 
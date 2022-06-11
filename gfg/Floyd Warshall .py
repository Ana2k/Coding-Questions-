#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		#https://www.youtube.com/watch?v=oNI0rf2P9gE&ab_channel=AbdulBari
		#explanation video by abdul bari useful link
		#for generating the matrix
		for k in range(n):
    		for i in range(n):
    		    for j in range(n):
    		        x = matrix[i][j] if matrix[i][j]!=-1 else float("inf")
    		        y = matrix[i][k] if matrix[i][k]!=-1 else float("inf")
    		        z = matrix[k][j] if matrix[k][j]!=-1 else float("inf")
    		        
    		        matrix[i][j] = min(x,y+z)


## First block in google colab
import numpy as np
a=np.array([1,2,3,4,5])
print(a)

## end of first block in colab


## start of second block in colab

import time
a=np.random.rand(1000000)

b=np.random.rand(1000000)

start=time.time()
c=np.dot(a,b)
end=time.time()

print("Vectorized time is: ")
print((end-start)*10000)

start=time.time()
c=0
for i in range(1000000):
    c+=a[i]*b[i]
end=time.time()

print("Forloop time is: ")
print((end-start)*10000)


## end of second block in colab
# # class Solution_brute_force:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         rowStart = 0
#         colStart = 0
#         rowEnd = len(matrix)-1
#         colEnd = len(matrix[0])-1
        
#         if not matrix:
#             return []
        
#         res = []
#         while(rowStart<=rowEnd and colStart<=colEnd):
#             for i in range(colStart,colEnd+1):
#                 res.append(matrix[rowStart][i])
#             rowStart+=1
            
#             for i in range(rowStart,rowEnd+1):
#                 res.append(matrix[i][colEnd])
#             colEnd-=1
            
#             if rowStart<=rowEnd:
            
#                 for i in range(colEnd,colStart-1,-1):
#                     res.append(matrix[rowEnd][i])

#                 rowEnd-=1
            
#             if colStart<=colEnd:

#                 for i in range(rowEnd,rowStart-1,-1):
#                     res.append(matrix[i][colStart])

#                 colStart+=1
#         return res
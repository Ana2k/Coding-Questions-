#longer to write shorter complexity.
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        li = [p1,p2,p3,p4]
        li.sort()
        A,D,B,C = li[0],li[1],li[2],li[3]
        # D--- C
        # |    |
        # |    |
        # A--- B   square means dist(abs(B-A)==abs(C-B)==abs(D-C)==abs(D-A))
        #the biggest issue was with, same points.
        #and understanding that diagonal lengths must also be the same.
        
        xA,yA = A
        xB,yB = B
        xC,yC = C
        xD,yD = D
        
        flag = 1
        def findDistance(x1,x2,y1,y2):
            dist = int(((x2-x1)**2+(y2-y1)**2)**0.5)
            if dist==0:
                nonlocal flag
                flag = 0
            return dist
        distAB = findDistance(xA,xB,yA,yB)
        distBC = findDistance(xB,xC,yB,yC)
        distCD = findDistance(xC,xD,yC,yD)
        distAD = findDistance(xA,xD,yA,yD)
        #diagonals
        distAC = findDistance(xA,xC,yA,yC)
        distBD = findDistance(xB,xD,yB,yD)
        if flag==0:
            return False
        # print(distAB," ",distBC," ",distCD," ",distAD)
        # print(distAC," ",distBD)
        if distAB==distBC==distCD==distAD:
            if distAC==distBD:
                return True
        return False

#Shorter to write, much longer time complexity
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # p4--- p3
        # |    |
        # |    |
        # p1--- p2   square means dist(abs(B-A)==abs(C-B)==abs(D-C)==abs(D-A))
        #for diagonals they must be equal and >sides
        st = set()
        li = [p1,p2,p3,p4]
        def findDistance(p,q):
            x1,y1 = p[0],p[1]
            x2,y2 = q[0],q[1]
            dist = ((x2-x1)**2+(y2-y1)**2)
            # print(dist,end = " ")
            return dist
        for i in range(4):
            for j in range(i+1,4):
                di = findDistance(li[i],li[j])
                if di!=0:
                    st.add(di)
                else:
                    return False
            # print()
        return len(st)==2
#Leetcode
#1 - i python always, seems only with using sorting.
def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:       
        diff = [(abs(el-x),el) for el in arr]
        heapq.heapify(diff)
        res = []
        while(k):
            curr = heapq.heappop(diff)
            res.append(curr[1])
            k-=1
        res.sort()
        return res

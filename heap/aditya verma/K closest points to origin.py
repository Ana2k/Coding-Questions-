#leetcode
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for x,y in points:
            #put the distance, x,y points into the heap
            heapq.heappush(heap,((x*x+y*y),x,y))
        res = []
        while(k):
            curr = heapq.heappop(heap)
            res.append([curr[1],curr[2]])
            k-=1
        return res
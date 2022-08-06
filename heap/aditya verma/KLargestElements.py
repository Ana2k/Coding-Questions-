import heapq
class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        heap = []
        heapq.heapify(heap)
        for x in li:
            heapq.heappush(heap,-x)
        res = []
        for i in range(k):
            res.append(-heapq.heappop(heap))
        return res
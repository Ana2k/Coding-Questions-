#User function Template for python3
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        heapq.heapify(arr)
        # print(heap)

        while(k-1):
            heapq.heappop(arr)
            k-=1
        return heapq.heappop(arr)
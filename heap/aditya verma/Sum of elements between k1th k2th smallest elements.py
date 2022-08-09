import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        def kthSmallest(k):
            arr = A[::]
            heapq.heapify(arr)
            # print(arr)
            #minheap
            while(k-1):
                heapq.heappop(arr)
                k-=1
            return heapq.heappop(arr)
        first = kthSmallest(K1)
        second = kthSmallest(K2)
        #now traverse once
        res = 0
        for i in range(len(A)):
            if(first<A[i]<second):
                res+=A[i]
        return res
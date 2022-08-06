#leetcode--> 6
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #concept of max-heap
        #largest ---> max heap
        di  = Counter(nums)
        
        heap = []
        #each call to heapify cost logn, n being the number of elements.
        heapq.heapify(heap)
        for key,val in di.items():
            #costs logn
            heapq.heappush(heap,(-1*val,key))

        res = []
        while(k):
            # print(heap)
            #costs logn
            curr = heapq.heappop(heap)
            # print(curr," ",k)
            res.append(curr[1])
            k-=1
        return res
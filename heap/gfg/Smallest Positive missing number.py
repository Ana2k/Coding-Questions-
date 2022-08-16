import heapq
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        res = 1
        pos  = 0
        heap = []
        heapq.heapify(heap)
        st = set()
        for x in arr:
            if x>0 and x not in st:
                heapq.heappush(heap,x)
                st.add(x)
                pos+=1
        #now that is a minheap.
        # print(heap)
        while(pos):
            curr = heapq.heappop(heap)
            if res==curr:
                res = curr+1
            else:
                return res
            pos-=1
        return res
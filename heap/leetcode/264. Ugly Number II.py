class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # https://leetcode.com/problems/ugly-number-ii/discuss/718866/Python-solution-Explained-Simple-to-follow-Different-Approach
        #one thing that we do understand is, we can only have the multiples of 2,3,5
        #the next thing needed is, to keep a track so that we dont over count
        #how do we deal with this the 
        # question arises this right?
        #  we use a set by the side so that we dont repeat values in our heap,
        #  now the topmost value of our heap will be the answer
        heap = [1]
        seen = {1}
        
        for i in range(n-1):
            curr = heapq.heappop(heap)
            if curr*2 not in seen:
                seen.add(curr*2)
                heapq.heappush(heap,curr*2)
            if curr*3 not in seen:
                seen.add(curr*3)
                heapq.heappush(heap,curr*3)
            if curr*5 not in seen:
                seen.add(curr*5)
                heapq.heappush(heap,curr*5)
        return heapq.heappop(heap)
            
            
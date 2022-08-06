#leetcode --- #7
class Solution:
    def frequencySort(self, s: str) -> str:
        di = Counter(s)
        #it wont strike immediately that this is a heap kind of question.
        heap = []
        heapq.heapify(heap)
        for key,val in di.items():
            heapq.heappush(heap,(-1*val,key))
        # n = len(s)
        res = ""
        # print(heap)
        while(len(heap)):
            val,ch = heapq.heappop(heap)
            res+=(ch*(-1*val))
        return res
#GFG --- #7
import heapq
from collections import Counter
t = int(input())
while(t):
    n = int(input())
    li = list(map(int,input().split()))
    di = Counter(li)
    heap = []
    heapq.heapify(heap)
    for k,v in di.items():
        heapq.heappush(heap,(-1*v,k))
    res = []
    while(len(heap)):
        val,k = heapq.heappop(heap)
        res+=[k]*(-1*val)
    print(*res)
    t-=1
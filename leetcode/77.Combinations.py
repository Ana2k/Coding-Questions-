#itertools
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1),k))
        
#backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #backtracking
        res = []
        def comb(num,curr,k):
            if k==0:
                res.append(curr)
                return
            for i in range(num,n+1):
                comb(i+1,curr+[i],k-1)
            return
        comb(1,[],k)
        return res
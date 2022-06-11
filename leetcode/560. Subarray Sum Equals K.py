#previous question. similar to 1658
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = count = 0
        di = Counter()
        di[0] = 1
        #if prefix=k? then prefix-k = 0 
        #we were doing count+=1 then so we just manually input that.
        for x in nums:
            prefix+=x
            count+=di[prefix-k]
            di[prefix]+=1
        return count            
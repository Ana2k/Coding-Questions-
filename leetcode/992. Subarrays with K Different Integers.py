#sliding window practise
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def dfs(sz):
            count, left,di = 0,0, defaultdict(lambda : 0)
            len_di = 0
            
            for right in range(len(nums)):
                di[nums[right]]+=1
                while(len(di)>sz):
                    di[nums[left]]-=1
                    if di[nums[left]]==0:
                        del di[nums[left]]
                    left+=1                    
                count+=(right-left+1)
            return count

        return dfs(k)-dfs(k-1)
    
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/2111046/Python3-Simple-Sliding-Window-Based-Solution
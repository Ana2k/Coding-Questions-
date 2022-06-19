#sliding window practise
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def dfs(sz):
            nonlocal n
            right = left = count = 0
            di = defaultdict(lambda : 0)
            while(right<n):
                di[nums[right]]+=1
                while(len(di)>sz):
                    di[nums[left]]-=1
                    if di[nums[left]]==0:
                        del di[nums[left]]
                    left+=1
                count+=(right-left+1)
                right+=1
            return count

        return dfs(k)-dfs(k-1)
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/672979/Analysis-and-explanation-with-Visualization
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/2111046/Python3-Simple-Sliding-Window-Based-Solution
#sliding window practise
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def subs(k):
            nonlocal n
            right = left = count = 0
            #stores length of unique subarray so far.
            di = defaultdict(lambda : 0)
            while(right<n):
                di[nums[right]]+=1
                while(len(di)>k):
                    di[nums[left]]-=1
                    if di[nums[left]]==0:
                        #deleting this so we dont count it in len(di)
                        del di[nums[left]]
                    left+=1
                count+=(right-left+1)
                right+=1
            return count

        return subs(k)-subs(k-1)
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/672979/Analysis-and-explanation-with-Visualization
    # https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/2111046/Python3-Simple-Sliding-Window-Based-Solution
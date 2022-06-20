#sliding window
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # inspired from https://leetcode.com/problems/maximum-product-subarray/
        n = len(nums)
        res = left = 0
        prod = 1
        for right in range(n):
            prod = prod*nums[right]
            while(prod>=k and left<n):
                prod = prod//nums[left]
                left+=1
            if left<=right:
                res+=(right-left+1)
        return res
#Method 1 : Dp naive
#there is a metehod 2 with binary search and bisect modules....
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/2072645/Short-and-crisp-python-based-on-Binary-Search
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
# lost patience to the binary search part. in case you revisit give it a shot. :/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #great explanation by neetcode 
        # https://www.youtube.com/watch?v=cjWnW0hdF1Y&t=274s&ab_channel=NeetCode
        n = len(nums)
        LIS = [1]*(n+1)
        maxi = 1
        #so now we think of two pointers at some ith position(i moves towards 0) and 
        #and j starting from i+1th.(moves towards n)
        #we will check for each whether there is, 
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[j]+1,LIS[i]) 
        return max(LIS)
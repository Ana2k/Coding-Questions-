#DP METHOD 2(preferred):USING EASY RECURSION TO NORMAL DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #length of LIS = 1 ,for the smallest subsequence.
        #https://afteracademy.com/blog/longest-increasing-subsequence
        # best link for understanding the recursion to dp approach.
        # then greedy and further breaking down into binary search.
        
        #keeps track for every single element so far, what has been the longest subsequence
        n = len(nums)
        lis = [1]*(n)
        #if you think of the index i, what is the minimum max longest subsequence it can have?
        #you cant move back, that means it will be  1. That element itself.
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    lis[i] = max(lis[i],1+lis[j])
        return max(1,max(lis))    

# #Method 1 : Dp naive
# #there is a metehod 2 with binary search and bisect modules....
# # https://leetcode.com/problems/longest-increasing-subsequence/discuss/2072645/Short-and-crisp-python-based-on-Binary-Search
# # https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
# # lost patience to the binary search part. in case you revisit give it a shot. :/
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         #great explanation by neetcode 
#         # https://www.youtube.com/watch?v=cjWnW0hdF1Y&t=274s&ab_channel=NeetCode
#         n = len(nums)
#         LIS = [1]*(n+1)
#         maxi = 1
#         #so now we think of two pointers at some ith position(i moves towards 0) and 
#         #and j starting from i+1th.(moves towards n)
#         #we will check for each whether there is, 
#         for i in range(n-1,-1,-1):
#             for j in range(i+1,n):
#                 if nums[i]<nums[j]:
#                     LIS[i] = max(LIS[j]+1,LIS[i]) 
#         return max(LIS)
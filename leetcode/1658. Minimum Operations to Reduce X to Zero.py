#daily challenge june 11
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/2138502/JAVA-Detailed-Explanation-Easy-Solution-(Sliding-Window-)
        l = r = 0
        n = len(nums)
        ans = -1
        sumi = sum(nums)
        target = sumi-x
        currsum = 0
        while(r<n):
            currsum+=(nums[r])
            while(l<=r and currsum>target):
                currsum-=nums[l]
                l+=1
            if currsum==target:
                ans = max(ans,r-l+1)            
            r+=1
        res = -1 if ans==-1 else n-ans
        return res
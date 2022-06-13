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











# #Method 2 - same thing only
# class Solution:
# def subarraySum(self, nums: List[int], k: int) -> int:
#     #this link explains well this method
#     #https://leetcode.com/problems/subarray-sum-equals-k/discuss/1759909/C%2B%2Bor-Full-explained-every-step-w-Dry-run-or-O(n2)-greater-O(n)-or-Two-approaches
    
#     #basically how do we find the subarray sum? by prestoring it. 
#     # for array [1,2,3,4] we have prefix_sum = [1,3,6,10] then 
#     #for each subarray(j,i) we only need to do: sumi = prefix[i]-prefix[j] to find its sum
    
#     #now how to update the count? if prefix[i]==k then count+=1 
#     # (as that means from 1 till that number we have a target)
#     #then we also use a dictionary. di = Counter() in which we store each prefix[i]
#     #this will be useful for k = prefix[i]-prefix[j] then if di[prefix[i]-k] exists
#     #we add that to the count
#     n = len(nums)
#     prefix = [0]*(n)
#     prefix[0]= nums[0]
#     count = 0
#     for i in range(1,n):
#         prefix[i] = nums[i]+prefix[i-1]
#     di = Counter()
#     for i in range(n):
#         if prefix[i]==k:
#             count+=1
#         other_num = prefix[i]-k
#         count+=di[other_num]
#         di[prefix[i]]+=1
#     return count            
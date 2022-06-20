class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #we always need to check for duplicates.
        target = 0
        nums.sort()
        n = len(nums)
        res = []
        for i,ch in enumerate(nums):
            #remove any duplicates from i
            #key line for complexity management!
            if i>0 and nums[i-1]==ch:
                continue
            #now find a two sum between j and k
            j = i+1
            k = n-1
            while(j<k):
                curr_sum = nums[i]+nums[j]+nums[k]
                if curr_sum<target:
                    #then increase the lower pointer
                    j+=1
                elif curr_sum>target:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    #remove jth duplicates
                    #important step otherwise duplicates are also calculated.
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
        return res
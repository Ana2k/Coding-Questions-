class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 1
        while(i<j):
            if nums[i-1]==nums[j]:
                nums[i]=nums[j]
                i+=1
            j+=1
        return i
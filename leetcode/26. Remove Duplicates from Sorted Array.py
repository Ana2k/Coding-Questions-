class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 1
        #k = 1 so i-1 according to question.
        n = len(nums)
        while(j<n):
            if nums[i-1]!=nums[j]:
                nums[i]=nums[j]
                i+=1
            j+=1
        return i
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #would have just used counter khatam kahani. O_O
        #but constant extra space so the following.
        n = len(nums)
        idx = 0
        for i in range(n+1):
            # print(idx," ",i) - Two pointers
            # print(nums)
            if nums[idx]<0:
                return idx
            else:
                nums[idx] = -nums[idx]
                idx = abs(nums[idx])
        return -1
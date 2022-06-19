class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #three methods 1)nums.sort() 2)bubble sort 3)dutch-flag - binary swap/search
        low = mid = 0
        high = len(nums)-1
        # aim --> low==> keeps all 0, mid==> keeps all 1, hi==> keeps all 2
        while(mid<=high):
            if nums[mid]==0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==2:
                nums[high],nums[mid] = nums[mid],nums[high]
                high-=1
            else:
                #no swaps needed
                mid+=1
        return nums
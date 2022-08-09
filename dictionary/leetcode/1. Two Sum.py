from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = defaultdict(lambda : -1)
        for i in range(len(nums)):
            if di[target-nums[i]]!=-1:
                #means we found the other pair to this
                return [di[target-nums[i]],i]
            di[nums[i]] = i
        return [-1,-1]
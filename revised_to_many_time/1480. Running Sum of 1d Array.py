class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0
        return [count:=count+num for num in nums]
        
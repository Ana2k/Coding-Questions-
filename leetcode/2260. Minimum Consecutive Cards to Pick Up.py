#sliding window - nonn arsh sheet
#Method 2
class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        end = 0
        res = float("inf")
        di = defaultdict(lambda : -1)
        n = len(nums)
        for end in range(len(nums)):
            ch = nums[end]
            if di[ch]!=-1:
                res = min(res,end-di[ch]+1)
            di[ch] = end
        return res if res!=float("inf") else -1
#Method 1class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        start = end = 0
        res = float("inf")
        di = Counter()
        n = len(nums)
        while(end<n):
            di[nums[end]]+=1
            # print(nums[start:end+1]," ",end,":",di[end])
            while(start<=end and di[nums[end]]>1):
                res = min(res,end-start+1)
                di[nums[start]]-=1
                start+=1
            end+=1
        return res if res!=float("inf") else -1              
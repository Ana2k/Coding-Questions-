#Daily challenge june 12
#Using Sets
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #set
        n = len(nums)
        l = r = 0
        st = set()
        currsum = res = 0
        while(r<n):
            while(nums[r] in st and l<=r):
                st.remove(nums[l])
                currsum-=nums[l]
                l+=1
            currsum+=nums[r]
            res = max(res,currsum)
            st.add(nums[r])
            r+=1
        return res
#Using Dictionary
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #dictionary
        n = len(nums)
        l = r = 0
        di = Counter()
        currsum = res = 0
        while(r<n):
            di[nums[r]]+=1
            currsum+=nums[r]
            while(l<=r and di[nums[r]]>1):
                di[nums[l]]-=1
                currsum-=nums[l]
                l+=1
            res = max(res,currsum)
            r+=1
        return res            # print(nums[start:end+1]," ",currsum)

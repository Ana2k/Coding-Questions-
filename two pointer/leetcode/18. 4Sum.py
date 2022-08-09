class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n-3):
            if i>0 and nums[i-1]==nums[i]:
                # print("----if i",i)
                continue#skips over duplicates
            for k in range(i+1,n-2):
                if k>i+1 and nums[k-1]==nums[k]:
                    continue
                m,j = k+1,n-1
                while(m<j):
                    a,b,c,d = nums[i],nums[k],nums[m],nums[j]
                    # print(a," ",b," ",c," ",d," ")
                    curr_sum = a+b+c+d
                    if curr_sum<target:
                        m+=1
                    elif curr_sum>target:
                        j-=1
                    else:
                        res.append([a,b,c,d])
                        m+=1
                        while(m<j and nums[m]==nums[m-1]):
                            m+=1
            # print("1---i",i)
        return res
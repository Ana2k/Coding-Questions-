class Solution:
    def maxProduct(self, nums: List[int]) -> int:
#method 1
        n = len(nums)
        if n==1:
            return nums[0]
        res = math.prod(nums)
        if res>0:
            return res
        max_till_now = min_till_now = 1
        for num in nums:
            prod_max = max_till_now*num
            prod_min = min_till_now*num
            
            max_till_now = max(prod_max,prod_min,num)
            min_till_now = min(prod_max,prod_min,num)
            res= max(res,max_till_now)
        return res

#method 2
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #sliding window.     
        n = len(nums)
        res = float("-inf")
        prodForward = prodBackward = 1
        i=0
        j = n-1
        while(i<n):
            prodForward*=nums[i]
            if res<prodForward:
                res = prodForward
            if prodForward==0:
                prodForward=1
            i+=1
            
            prodBackward*=nums[j]
            if res<prodBackward:
                res = prodBackward
            if prodBackward==0:
                prodBackward=1
            j-=1
        return res

#method 3
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #sliding window. 
        # https://leetcode.com/problems/maximum-product-subarray/discuss/2080958/Java-Kadane's-algorithm-variant-O(n)-run-and-O(1)-space.
        # https://leetcode.com/problems/maximum-product-subarray/discuss/416395/JavaScript-Solution-w-Explanation
        n = len(nums)
        res = maxi = mini = nums[0]
        #checking discussion for this.
        for i in range(1,n):
            
            currMax = max(maxi*nums[i],mini*nums[i],nums[i])
            currMini = min(mini*nums[i],maxi*nums[i],nums[i])
            
            # print(currMax," ",currMini)
            
            maxi = currMax
            mini = currMini
            res = max(res,currMax)
        return res       
#Method - binary search approach
# PEnding
#Method - two pointers approach
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #O(n+m) -- brute first

        m = len(nums1)
        n = len(nums2)
        i=j = idx =0
        nums = []
        while(idx<(m+n) and i<m and j<n):
            ch1 = nums1[i]
            ch2 = nums2[j]
            if ch1<=ch2:
                nums.append(ch1)
                i+=1
            else:
                nums.append(ch2)
                j+=1    
            idx+=1
        #either of these has ended or both have.
        while(i<m):
            nums.append(nums1[i])
            i+=1
        while(j<n):
            nums.append(nums2[j])
            j+=1
        total = (m+n)
        mid = total//2
        if total%2:
            #only one median
            return float(nums[mid])
        else:
            return (nums[mid]+nums[mid-1])/2

#Python special sort and destroy the aim of the question
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #O(n+m) -- brute first
        m = len(nums1)
        n = len(nums2)
        nums = nums1+nums2
        nums.sort()
        total = (m+n)
        mid = total//2
        if total%2:
            #only one median
            return float(nums[mid])
        else:
            return (nums[mid]+nums[mid-1])/2

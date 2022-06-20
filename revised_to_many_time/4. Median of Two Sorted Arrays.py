#Method - binary search approach
# https://www.youtube.com/watch?v=q6IEA26hvXc&ab_channel=NeetCode

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        
        total = len(A)+len(B)
        half = total//2
        # nums1 has to be lesser than nums2
        if len(A)>len(B):
            A,B = B,A
        l,r = 0,len(A)-1
            
        #because a median always exists
        while True:
            #for A - i
            i = (l+r)//2
            #for B - j
            #cause of zero indexing -1
            j = (half-1)-(i+1)
            
            ARight = A[i+1] if i+1<len(A) else float("inf")
            ALeft = A[i] if i>=0 else float("-inf")
            
            BRight = B[j+1] if j+1<len(B) else float("inf")
            BLeft = B[j] if j>=0 else float("-inf")
            
            #if partition is correct
            if ALeft<=BRight and BLeft<=ARight:
                #odd
                if total%2:
                    return min(ARight,BRight)
                else:
                    return (max(ALeft,BLeft)+min(ARight,BRight))/2
            #update the partitions
            elif ALeft>BRight:
                #we need to reduce the A value how?
                #by changing the pointer.
                r = i-1
            else:
                l = i+1


#Method - two pointers approach
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #O(n+m) -- brute first

        m = len(nums1)
        n = len(nums2)
        i=j = idx =0
        nums = []
        while(idx<(m+n) and i<m and j<n):
            ch1  = nums1[i]
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

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #build it up from back
        i = m-1
        j = n-1
        idx = (m+n-1)
        while(idx>=0):
            ch1 = nums1[i] if i>=0 else float("-inf")
            ch2 = nums2[j] if j>=0 else float("-inf")
            if(ch1>=ch2):
                nums1[idx] = ch1
                i-=1
            else:
                nums1[idx] = ch2
                j-=1
            idx-=1
#Method 2
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s[::-1]==s else 2
        #can also do the same using two pointers.
#Method 1
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        #we have only two letters 
        #and we need to make use of the fact. 
        #that subsequences means just using two letters.
        #so if its empty strinng-> count= 0
        # if its a palindrome count = 1
        #if not a palindrome, remove all the as and all the bs....thus two steps
        #as its a subsequence
        for i in range(len(s)):
            if s[i]!=s[-(i+1)]:
                return 2        
        return 1

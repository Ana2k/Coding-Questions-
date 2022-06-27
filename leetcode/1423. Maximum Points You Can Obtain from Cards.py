#june 26
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597825/Simple-Clean-Intuitive-Explanation-with-Visualization
        #this post can be used for visualising the problem.
        n = len(cardPoints)
        res = sumi = sum(cardPoints[:k])
        left = k-1
        right = n-1
        while(left>=0):
            sumi-=cardPoints[left]
            sumi+=cardPoints[right]
            res = max(res,sumi)
            left-=1
            right-=1
        return res
        
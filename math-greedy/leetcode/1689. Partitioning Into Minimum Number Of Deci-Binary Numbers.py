# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/discuss/2202734/python-1-liner-with-explanation
# this is well explained :)
#Method 1
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(list(n)))
#Method 2
#well explained
class Solution:
    def minPartitions(self, n: str) -> int:
        #hint 1 says = if this was single digit add up ones as the number.
        # 3*10+2 = 3*10+1+1
        #82734 = 8*10000+2*1000+7*100+3*10+4
        #set of these = (10000,1000,100,10,1,1,1,1)
        #so the number of digits-1+last digit value
        # dp?
        #hint 2 saays : solve for each digit individually and merge their answers
        #3--> 3 answer, and 2--> answer = 2 but its visited at 3 so dont consider that
        #so the answer is max(of the number in this digit?)
        li = list(n)
        res = int(max(li))
        return res
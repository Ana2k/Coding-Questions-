class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #a different method https://leetcode.com/problems/gas-station/discuss/860396/Python-O(n)-greedy-solution-explained
        #this idea explained https://leetcode.com/problems/gas-station/discuss/1454600/Ideas-explained
        #for each station the formula is: gas[i]-cost[i]+gas[i+1]>=0
        if sum(gas)<sum(cost):
            return -1
        n,diff,start =  len(gas),0,0
        for i in range(n):
            diff += gas[i]-cost[i]
            #if the difference <0 meeans, we cant travel using the index wee were starting with
            #or we can say for start = A index and end = B, then (A+1,B) ...(A+(B-A-1)),B none of them will give us a proper answer
            #so we shift the index to i+1
            if diff<0:
                diff,start = 0,i+1
        return start              
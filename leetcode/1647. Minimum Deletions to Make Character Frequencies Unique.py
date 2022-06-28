#june 28 daily challenge
#used hints till level 3
class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        visited = []
        res = 0
        st = set(s)
        for ch in st:
            freq = count[ch]
            if freq not in val:
                visited.append(freq)
            else:
                #keep adding to res, and 
                #keep decreasing the freq
                while(freq):
                    res+=1
                    freq-=1
                    if freq not in visited:
                        visited.append(freq)
                        break      
        return res
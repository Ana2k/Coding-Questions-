#daily challenge June 20
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        #trie this trie :)
        # https://leetcode.com/problems/short-encoding-of-words/discuss/2172401/Python-Concise-Brute-Force-and-Trie-Solutions-with-Explanation
        words = set(words)
        #to keep track of all the suffixes
        di = Counter()
        for word in words:
            for i in range(len(word)):
                suff = word[i:]
                di[suff]+=1
        res = 0
        for word in words:
            if di[word]==1:
                res += len(word)+1
        return res
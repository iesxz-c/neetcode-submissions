class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        res=""
        n=len(word1)
        m = len(word2)
        while i<min(m,n):
            res+=word1[i]+word2[i]
            i+=1

        for j in range(i,n):
                res+=word1[j]
        for j in range(i,m):
            res+=word2[j]
        return res
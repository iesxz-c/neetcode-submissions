class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0

        res=""
        minle = min(len(word1),len(word2))
        while i<minle:
            res+=word1[i]
            res+=word2[j]
            i+=1
            j+=1
        res+=word1[i:]
        res+=word2[j:]
        return res

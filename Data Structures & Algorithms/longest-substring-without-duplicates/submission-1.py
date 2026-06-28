class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        se = set()
        le=0
        maxll=0
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            le=r-l+1
            maxll = max(maxll,le)
           
        return maxll
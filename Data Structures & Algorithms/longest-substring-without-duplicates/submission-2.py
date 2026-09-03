class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se={}
        l=0
        ans=0
        for r in range(len(s)):
            se[s[r]] = se.get(s[r],0)+1
            while se[s[r]] > 1:
                se[s[l]] -=1
                l+=1
            ans = max(ans,r-l+1)
        return ans
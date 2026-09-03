class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a={}
        ans=0
        l=0
        maxfreq=0
        for r in range(len(s)):
            a[s[r]] = a.get(s[r],0)+1
            maxfreq=max(maxfreq,a[s[r]])
            while (r-l+1) - maxfreq >k:
                a[s[l]] -=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
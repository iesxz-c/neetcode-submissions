from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc=Counter(t)
        c=len(tc)
        ans = ""
        l=0
        formed=0
        have={}
        for r in range(len(s)):
            have[s[r]] = have.get(s[r],0)+1
            if have[s[r]] == tc[s[r]]:
                formed+=1
            while formed == c:
                if not ans or len(ans) > len( s[l:r+1]):
                    ans = "".join(s[l:r+1])
                have[s[l]] -=1
                if s[l] in tc and have[s[l]] < tc[s[l]]:
                    formed -= 1
                l+=1
        return ans

            
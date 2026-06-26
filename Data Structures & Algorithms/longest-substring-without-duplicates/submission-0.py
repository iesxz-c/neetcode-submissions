class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        lon =0
        state = set()
        for  i in range(len(s)):
            while s[i] in state:
                state.remove(s[l])
                l+=1
            state.add(s[i])
            
            lon = max(lon,i-l+1)
        return lon
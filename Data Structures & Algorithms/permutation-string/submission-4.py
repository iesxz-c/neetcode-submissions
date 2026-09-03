from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = Counter(s1)
        l=0
        s2c={}
        for r in range(len(s2)):
            s2c[s2[r]] =s2c.get(s2[r],0)+1
            if r-l+1 == len(s1):
                if s1c ==s2c:
                    return True
                s2c[s2[l]]-=1
                if s2c[s2[l]]  == 0:
                    del s2c[s2[l]]
                l+=1
        return False
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        k=Counter(s1)
        w=[]
        l=0
        
        for r in range(len(s2)):
            w.append(s2[r])
            
            if r-l+1 == len(s1):
                if Counter(w) == k:
                    return True
                else:
                    del w[0]
                    l+=1
        return False
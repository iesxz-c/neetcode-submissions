class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        w=[]
        minc=float('inf')
        for r in range(len(blocks)):
            w.append(blocks[r])
            if r-l+1 == k:
                minc = min(minc,w.count('W'))
                w.remove(blocks[l])
                l+=1
        return minc
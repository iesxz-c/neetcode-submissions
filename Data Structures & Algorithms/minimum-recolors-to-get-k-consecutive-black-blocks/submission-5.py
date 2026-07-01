class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # l=0
        # ans = float('inf')
        # whites =0
        # for r in range(len(blocks)):
        #     if blocks[r] == 'W':
        #         whites+=1
        #     if r-l+1 == k:
        #         ans = min(ans,whites)
        #         if blocks[l] == 'W':
        #             whites -= 1
        #         l+=1
        # return ans

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
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        minn =float('inf')
        whites =0
        blacks =0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                whites+=1
            else:
                blacks+=1

            if r-l+1 == k:
                minn = min(minn,whites)
                if blocks[l] == 'W':
                    whites-=1
                l+=1
        return minn
                                     
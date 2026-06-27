class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satis =0
        w=0
        maxw=0
        l=0
        for r in range(len(customers)):
            if grumpy[r]:
                w+=customers[r]
            else:
                satis += customers[r]
            
            if r-l+1 > minutes:
                if grumpy[l]:
                    w-=customers[l]
                l+=1
            maxw = max(maxw,w)
        return satis+maxw
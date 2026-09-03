class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        satis =0
        w =0
        maxw=0
        for r in range(len(customers)):
            if grumpy[r] == 0:
                satis += customers[r]
            else:
                maxw += customers[r]
            if r-l+1 > minutes:
                
                if grumpy[l] :
                    maxw -= customers[l]
                l+=1
                w= max(w,maxw)
        return w+satis
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        satis =0
        w=0
        maxx=0
        for r in range(len(customers)):
            if grumpy[r] == 1:
                w+=customers[r]
            else:
                satis += customers[r]
            if r-l+1 > minutes:
                if grumpy[l]:
                    w-=customers[l]
                l+=1
                maxx = max(maxx,w)
        return satis+maxx
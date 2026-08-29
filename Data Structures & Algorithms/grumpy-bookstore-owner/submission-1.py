class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satis =0
        for i,j in zip(customers,grumpy):
            if j==0 :satis+=1
        return satis